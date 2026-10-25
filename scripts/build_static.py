#!/usr/bin/env python3
"""Generate the static art: assets/banner.svg and the section headers. Run from the repo root."""
from pathlib import Path

from spacelib import BASE_CSS, MONO, NEBULA_BG_DEFS, SANS, nebula_layers, starfield

ASSETS = Path(__file__).resolve().parent.parent / "assets"

BANNER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-labelledby="t d">
<title id="t">Arun Prakash</title>
<desc id="d">Software architect and engineer in Kerala, India, working on AI agents, Rust and Flutter.</desc>
<defs>
<clipPath id="card"><rect width="1000" height="300" rx="18"/></clipPath>
@@NEBULA@@
<radialGradient id="planet" cx="35%" cy="30%" r="80%">
  <stop offset="0" stop-color="#fcd9a8"/><stop offset=".35" stop-color="#e58b6d"/><stop offset=".7" stop-color="#7b3f9e"/><stop offset="1" stop-color="#1b1245"/>
</radialGradient>
<linearGradient id="ring" x1="0" x2="1">
  <stop offset="0" stop-color="#a78bfa" stop-opacity=".25"/><stop offset=".5" stop-color="#e9d5ff" stop-opacity=".95"/><stop offset="1" stop-color="#67e8f9" stop-opacity=".35"/>
</linearGradient>
<linearGradient id="name" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4b5fd"/></linearGradient>
<linearGradient id="trail" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
</defs>
<style>
@@BASE_CSS@@
.fade{animation:fade 1.2s ease-out backwards}
@keyframes fade{from{opacity:0}}
.blink{animation:blink 1.1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.pulse{animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}
.shoot{animation:shoot 9s ease-in infinite;opacity:0}
@keyframes shoot{0%{transform:translate(0,0);opacity:0}4%{opacity:1}16%{transform:translate(300px,135px);opacity:0}100%{transform:translate(300px,135px);opacity:0}}
</style>
<g clip-path="url(#card)">
@@LAYERS@@
@@STARS@@
<circle cx="790" cy="150" r="92" fill="#7c5cff" opacity=".28" filter="url(#glow)"/>
<g transform="rotate(-16 790 150)">
  <ellipse cx="790" cy="150" rx="128" ry="30" fill="none" stroke="url(#ring)" stroke-width="6"/>
  <ellipse cx="790" cy="150" rx="108" ry="25" fill="none" stroke="url(#ring)" stroke-width="2" opacity=".5"/>
  <circle cx="790" cy="150" r="64" fill="url(#planet)"/>
  <path d="M662 150 A128 30 0 0 0 918 150" fill="none" stroke="url(#ring)" stroke-width="6"/>
  <path d="M682 150 A108 25 0 0 0 898 150" fill="none" stroke="url(#ring)" stroke-width="2" opacity=".5"/>
  <ellipse cx="790" cy="150" rx="200" ry="90" fill="none" stroke="#c4b5fd" stroke-opacity=".12" stroke-dasharray="2 6"/>
  <circle r="9" fill="#e0f2fe" opacity=".35" filter="url(#glow)"><animateMotion dur="16s" repeatCount="indefinite" path="M590,150 a200,90 0 1,0 400,0 a200,90 0 1,0 -400,0"/></circle>
  <circle r="5" fill="#e0f2fe"><animateMotion dur="16s" repeatCount="indefinite" path="M590,150 a200,90 0 1,0 400,0 a200,90 0 1,0 -400,0"/></circle>
</g>
<g transform="translate(110,14)"><g class="shoot"><line x1="-70" y1="-31" x2="0" y2="0" stroke="url(#trail)" stroke-width="2" stroke-linecap="round"/></g></g>
<g class="fade" style="animation-delay:.1s">
  <circle class="pulse" cx="62" cy="76" r="3.5" fill="#4ade80"/>
  <text x="78" y="80" font-family="@@MONO@@" font-size="13" letter-spacing="3" fill="#7dd3fc" textLength="338" lengthAdjust="spacing">KERALA, INDIA · 9.26°N 76.78°E</text>
</g>
<text class="fade" style="animation-delay:.3s" x="56" y="152" font-family="@@SANS@@" font-size="62" font-weight="800" fill="url(#name)" textLength="520" lengthAdjust="spacing">ARUN PRAKASH</text>
<text class="fade" style="animation-delay:.6s" x="58" y="196" font-family="@@SANS@@" font-size="24" fill="#e2e8f0">Software architect &amp; engineer</text>
<g class="fade" style="animation-delay:.9s">
  <text x="58" y="230" font-family="@@MONO@@" font-size="15" fill="#94a3b8" textLength="306" lengthAdjust="spacing">AI agents · Rust · Flutter · cloud</text>
  <rect class="blink" x="372" y="217" width="9" height="16" fill="#a78bfa"/>
</g>
</g>
</svg>
"""

HEADER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 48" width="1000" height="48" role="img" aria-label="@@TITLE@@">
<defs>
<linearGradient id="l" x1="0" x2="1"><stop offset="0" stop-color="#8b5cf6" stop-opacity="0"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>
<linearGradient id="r" x1="0" x2="1"><stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></linearGradient>
<linearGradient id="tx" x1="0" x2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
</defs>
<style>
@@BASE_CSS@@
</style>
<rect x="@@LX@@" y="23" width="@@LW@@" height="1.5" fill="url(#l)"/>
<circle class="tw" cx="@@LDOT@@" cy="24" r="2.6" fill="#8b5cf6"/>
<text x="500" y="30" text-anchor="middle" font-family="@@MONO@@" font-size="17" font-weight="700" letter-spacing="6" fill="url(#tx)">@@TITLE@@</text>
<circle class="tw" cx="@@RDOT@@" cy="24" r="2.6" fill="#22d3ee" style="animation-delay:1.5s"/>
<rect x="@@RX@@" y="23" width="@@LW@@" height="1.5" fill="url(#r)"/>
</svg>
"""

HEADERS = {
    "transmission": "TRANSMISSION",
    "orbit": "CURRENT ORBIT",
    "constellations": "CONSTELLATIONS",
    "instruments": "INSTRUMENT PANEL",
    "channel": "OPEN CHANNEL",
}


def banner():
    svg = BANNER
    for key, val in {
        "@@NEBULA@@": NEBULA_BG_DEFS,
        "@@BASE_CSS@@": BASE_CSS,
        "@@LAYERS@@": nebula_layers(1000, 300),
        "@@STARS@@": starfield(1000, 300, 150, seed=310, keep_out=(40, 60, 640, 250)),
        "@@MONO@@": MONO,
        "@@SANS@@": SANS,
    }.items():
        svg = svg.replace(key, val)
    return svg


def header(title):
    half = 8.5 * len(title) + 26  # approx half text width incl. letter-spacing
    gap = 22
    left_end = 500 - half - gap
    right_start = 500 + half + gap
    line_w = left_end - 40
    svg = HEADER
    for key, val in {
        "@@TITLE@@": title,
        "@@BASE_CSS@@": BASE_CSS,
        "@@MONO@@": MONO,
        "@@LX@@": f"{40:.1f}",
        "@@LW@@": f"{line_w:.1f}",
        "@@LDOT@@": f"{left_end:.1f}",
        "@@RDOT@@": f"{right_start:.1f}",
        "@@RX@@": f"{right_start + 4:.1f}",
    }.items():
        svg = svg.replace(key, val)
    # right line must end at x=960 regardless of title length
    svg = svg.replace(f'x="{right_start + 4:.1f}" y="23" width="{line_w:.1f}"', f'x="{right_start + 4:.1f}" y="23" width="{960 - right_start - 4:.1f}"')
    return svg


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "banner.svg").write_text(banner(), encoding="utf-8")
    for name, title in HEADERS.items():
        (ASSETS / f"h-{name}.svg").write_text(header(title), encoding="utf-8")
    print("wrote banner +", len(HEADERS), "headers")
