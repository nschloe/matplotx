"""
https://github.com/atom/atom/blob/master/packages/one-dark-syntax/styles/colors.less
https://github.com/joshdick/onedark.vim/blob/main/colors/onedark.vim
"""
from ._helpers import generate_style

onedark = generate_style(
    background="#282c34",
    foreground="#abb2bf",
    comment="#5c6370",
    cycle=[
        "#61afef",  # blue
        "#d49f6e",  # orange 1
        "#98c379",  # green
        "#e06c75",  # red 1
        "#c678dd",  # purple
        # "",  # pink
        # "",  # comment
        "#e5c07b",  # yellow
        "#36aaba",  # cyan
    ],
)
