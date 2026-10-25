#!/usr/bin/env python3
"""Refresh assets/stats.svg from the GitHub API. Run from anywhere; uses GITHUB_TOKEN if set."""
import json
import os
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

from spacelib import BASE_CSS, MONO, NEBULA_BG_DEFS, SANS, nebula_layers, starfield

USER = "ArunPrakashG"
OUT = Path(__file__).resolve().parent.parent / "assets" / "stats.svg"
LANG_COLORS = {
    "Dart": "#00b4ab", "Rust": "#dea584", "C#": "#38a169", "Python": "#3572a5", "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a", "PHP": "#8892bf", "Go": "#00add8", "Kotlin": "#a97bff", "Swift": "#f05138",
    "Shell": "#89e051", "HTML": "#e34c26", "CSS": "#8b6bd6", "C++": "#f34b7d", "Java": "#b07219",
}


def get(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch():
    profile = get(f"/users/{USER}")
    repos, page = [], 1
    while True:
        batch = get(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    pushed = {r["name"]: datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00")) for r in own}
    last_push = max(pushed.values())
    cutoff = last_push - timedelta(days=730)  # languages reflect recent work, not old libraries
    langs = Counter(r["language"] for r in own if r["language"] and pushed[r["name"]] >= cutoff)
    return {
        "repos": len(own),
        "stars": sum(r["stargazers_count"] for r in own),
        "followers": profile["followers"],
        "last_push": last_push,
        "langs": langs.most_common(5),
    }


def tile(x, value, label):
    return (
        f'<text x="{x}" y="118" font-family="{SANS}" font-size="44" font-weight="800" fill="url(#num)">{value}</text>'
        f'<text x="{x}" y="144" font-family="{MONO}" font-size="12" letter-spacing="2.5" fill="#94a3b8">{label}</text>'
    )


def render(d):
    total = sum(n for _, n in d["langs"]) or 1
    bar, legend, x, lx = [], [], 56.0, 56
    full = 888.0
    for i, (lang, n) in enumerate(d["langs"]):
        w = full * n / total
        color = LANG_COLORS.get(lang, "#94a3b8")
        bar.append(f'<rect x="{x:.1f}" y="206" width="{max(w - 3, 2):.1f}" height="10" rx="5" fill="{color}"/>')
        pct = round(100 * n / total)
        legend.append(
            f'<circle cx="{lx + 5}" cy="246" r="5" fill="{color}"/>'
            f'<text x="{lx + 18}" y="250" font-family="{MONO}" font-size="13" fill="#cbd5e1">{lang} <tspan fill="#64748b">{pct}%</tspan></text>'
        )
        x += w
        lx += 180
    tiles = "".join(
        [
            tile(56, d["repos"], "OPEN REPOS"),
            tile(292, d["stars"], "STARS EARNED"),
            tile(528, d["followers"], "FOLLOWERS"),
            tile(764, d["last_push"].strftime("%d %b"), "LAST PUSH"),
        ]
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 290" width="1000" height="290" role="img" aria-label="GitHub mission log: {d['repos']} open repos, {d['stars']} stars, {d['followers']} followers">
<defs>
<clipPath id="card"><rect width="1000" height="290" rx="18"/></clipPath>
{NEBULA_BG_DEFS}
<linearGradient id="num" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4b5fd"/></linearGradient>
</defs>
<style>{BASE_CSS}</style>
<g clip-path="url(#card)">
{nebula_layers(1000, 290)}
{starfield(1000, 290, 110, seed=7, keep_out=(40, 40, 960, 260))}
<text x="56" y="52" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="4" fill="#7dd3fc">MISSION LOG</text>
<text x="944" y="52" text-anchor="end" font-family="{MONO}" font-size="12" fill="#64748b">synced {date.today().isoformat()}</text>
{tiles}
<text x="56" y="192" font-family="{MONO}" font-size="12" letter-spacing="2.5" fill="#94a3b8">FUEL GAUGE · LANGUAGES, LAST 2 YEARS</text>
{''.join(bar)}
{''.join(legend)}
</g>
</svg>
"""


if __name__ == "__main__":
    OUT.write_text(render(fetch()), encoding="utf-8")
    print("wrote", OUT)
