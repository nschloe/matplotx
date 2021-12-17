"""
https://github.com/morhetz/gruvbox
https://github.com/morhetz/gruvbox/blob/master/colors/gruvbox.vim
"""
from ._helpers import generate_style

gruvbox = {
    "dark": generate_style(
        foreground="#ebdbb2",  # light 1
        background="#282828",  # dark 0
        comment="#7c6f64",  # dark 4
        cycle=[
            "#458588",  # neutral_blue
            "#d65d0e",  # neutral_orange
            "#98971a",  # neutral_green
            "#cc241d",  # neutral_red
            "#b16286",  # neutral_purple
            "#d79921",  # neutral_yellow
            "#a89984",  # light4
            "#689d6a",  # neutral_aqua
        ],
    ),
    "light": generate_style(
        foreground="#3c3836",  # dark 1
        background="#fbf1c7",  # light 0
        comment="#a89984",  # light 4
        cycle=[
            "#458588",  # neutral_blue
            "#d65d0e",  # neutral_orange
            "#98971a",  # neutral_green
            "#cc241d",  # neutral_red
            "#b16286",  # neutral_purple
            "#d79921",  # neutral_yellow
            "#7c6f64",  # dark 4
            "#689d6a",  # neutral_aqua
        ],
    ),
}
