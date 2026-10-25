"""Shared helpers for the profile's generated SVG art."""
import random

STAR_COLORS = ["#ffffff", "#ffffff", "#bae6fd", "#fde68a", "#ddd6fe"]

# Fades back in from opacity 0 without forcing it to stay 0 when motion is disabled.
BASE_CSS = """
.tw{animation:tw 4s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.2}50%{opacity:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
"""

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"


def starfield(width, height, count, seed, keep_out=None):
    """Deterministic scatter of stars; ~60% twinkle. keep_out=(x0,y0,x1,y1) thins stars behind text."""
    rng = random.Random(seed)
    stars = []
    while len(stars) < count:
        x = rng.uniform(4, width - 4)
        y = rng.uniform(4, height - 4)
        if keep_out and keep_out[0] <= x <= keep_out[2] and keep_out[1] <= y <= keep_out[3] and rng.random() < 0.8:
            continue
        r = rng.choice([0.6, 0.8, 1.0, 1.3, 1.7])
        color = rng.choice(STAR_COLORS)
        if rng.random() < 0.6:
            delay = rng.uniform(0, 6)
            dur = rng.uniform(2.5, 6)
            stars.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" class="tw" '
                f'style="animation-delay:{delay:.1f}s;animation-duration:{dur:.1f}s"/>'
            )
        else:
            op = rng.uniform(0.35, 0.9)
            stars.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="{op:.2f}"/>')
    return "\n".join(stars)


NEBULA_BG_DEFS = """
<radialGradient id="bg" cx="75%" cy="45%" r="95%">
  <stop offset="0" stop-color="#1a1f4a"/><stop offset=".55" stop-color="#0a0d24"/><stop offset="1" stop-color="#04050e"/>
</radialGradient>
<radialGradient id="neb1"><stop offset="0" stop-color="#7c5cff" stop-opacity=".45"/><stop offset="1" stop-color="#7c5cff" stop-opacity="0"/></radialGradient>
<radialGradient id="neb2"><stop offset="0" stop-color="#22d3ee" stop-opacity=".28"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="neb3"><stop offset="0" stop-color="#f472b6" stop-opacity=".22"/><stop offset="1" stop-color="#f472b6" stop-opacity="0"/></radialGradient>
"""


def nebula_layers(width, height):
    return (
        f'<rect width="{width}" height="{height}" fill="url(#bg)"/>'
        f'<circle cx="{width*0.76:.0f}" cy="{height*0.4:.0f}" r="{height*0.87:.0f}" fill="url(#neb1)"/>'
        f'<circle cx="{width*0.98:.0f}" cy="{height*0.97:.0f}" r="{height*0.73:.0f}" fill="url(#neb2)"/>'
        f'<circle cx="{width*0.12:.0f}" cy="{height:.0f}" r="{height*0.67:.0f}" fill="url(#neb3)" opacity=".5"/>'
    )
