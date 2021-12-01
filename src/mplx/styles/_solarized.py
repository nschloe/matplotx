"""
https://ethanschoonover.com/solarized/
"""
from ._helpers import generate_style

cycle = [
    "268bd2",  # blue
    "cb4b16",  # orange
    "859900",  # green
    "dc322f",  # red
    "6c71c4",  # violet
    "d33682",  # magenta
    "586e75",  # base01
    "b58900",  # yellow
    "2aa198",  # cyan
]

solarized = {
    "dark": generate_style(
        foreground="839496",  # base0
        background="002b36",  # base03
        cycle=cycle,
    ),
    "light": generate_style(
        foreground="657b83",  # base00
        background="fdf6e3",  # base3
        cycle=cycle,
    ),
}
