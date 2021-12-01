"""
https://github.com/atom/atom/blob/master/packages/one-dark-syntax/styles/colors.less
"""
from ._helpers import generate_style


dracula = generate_style(
    background="282c34",
    foreground="abb2bf",
    cycle=[
        "61afef",  # blue
        "d49f6e",  # orange 1
        "98c379",  # green
        "e06c75",  # red 1
        "c678dd",  # purple
        # "",  # pink
        # "",  # comment
        "e5c07b",  # yellow
        "36aaba",  # cyan
    ],
)
