"""
https://github.com/morhetz/gruvbox
"""
from ._helpers import generate_style

gruvbox = {
    "dark": generate_style(
        foreground="ebdbb2",
        background="282828",
        cycle=[
            "458588",  # blue
            "d65d0e",  # orange
            "98971a",  # green
            "cc241d",  # red
            "b16286",  # purple
            "d79921",  # yellow
            "a89984",  # gray
            "689d6a",  # aqua
        ],
    ),
    "light": generate_style(
        foreground="3c3836",
        background="fbf1c7",
        cycle=[
            "458588",  # blue
            "d65d0e",  # orange
            "98971a",  # green
            "cc241d",  # red
            "b16286",  # purple
            "d79921",  # yellow
            "7c6f64",  # gray
            "689d6a",  # aqua
        ],
    ),
}
