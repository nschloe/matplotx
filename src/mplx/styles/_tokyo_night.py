"""
https://github.com/folke/tokyonight.nvim
https://github.com/folke/tokyonight.nvim/blob/main/lua/tokyonight/colors.lua
"""
from ._helpers import generate_style

tokyo_night = {
    # https://github.com/folke/tokyonight.nvim/blob/main/extras/alacritty_tokyonight_storm.yml
    "storm": generate_style(
        background="24283b",
        foreground="c0caf5",
        cycle=[
            "7aa2f7",  # blue
            "ff9e64",  # orange
            "9ece6a",  # green
            "f7768e",  # red
            "9d7cd8",  # purple
            "bb9af7",  # magenta
            "565f89",  # comment
            "e0af68",  # yellow
            "7dcfff",  # cyan
        ],
    ),
    "night": generate_style(
        background="1a1b26",
        foreground="c0caf5",
        cycle=[
            "7aa2f7",  # blue
            "ff9e64",  # orange
            "9ece6a",  # green
            "f7768e",  # red
            "9d7cd8",  # purple
            "bb9af7",  # magenta
            "565f89",  # comment
            "e0af68",  # yellow
            "7dcfff",  # cyan
        ],
    ),
    "day": generate_style(
        background="e1e2e7",
        foreground="3760bf",
        cycle=[
            "2e7de9",  # blue
            "b15c00",  # orange
            "587539",  # green
            "f52a65",  # red
            "7847bd",  # purple
            "9854f1",  # magenta
            "848cb5",  # comment
            "8c6c3e",  # yellow
            "007197",  # cyan
        ],
    ),
}
