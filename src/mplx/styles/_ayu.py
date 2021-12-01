"""
https://github.com/ayu-theme
"""
from ._helpers import generate_style

# https://github.com/ayu-theme/ayu-vim/blob/master/colors/ayu.vim
ayu = {
    "dark": generate_style(
        background="0F1419",
        foreground="E6E1CF",
        cycle=[
            "36A3D9",  # blue
            "FFB454",  # orange
            "95E6CB",  # green
            "F07178",  # red
            "5C6773",  # gray
            "FFEE99",  # yellow
        ],
    ),
    "light": generate_style(
        background="FAFAFA",
        foreground="5C6773",
        cycle=[
            "36A3D9",  # blue
            "F29718",  # orange
            "86B300",  # green
            "F07178",  # red
            "A37ACC",  # purple
            "ABB0B6",  # gray
            "4CBF99",  # cyan
        ],
    ),
    "mirage": generate_style(
        background="212733",
        foreground="D9D7CE",
        cycle=[
            "80D4FF",  # blue
            "FFD57F",  # orange
            "BBE67E",  # green
            "F07178",  # red
            "D4BFFF",  # purple
            "5C6773",  # gray
            "95E6CB",  # cyan
        ],
    ),
}
