"""
https://www.nordtheme.com/
"""
from ._helpers import generate_style

nord = generate_style(
    background="#2E3440",  # nord0
    foreground="#D8DEE9",  # nord4
    # comment="#4C566A",  # nord3
    # comment="#81A1C1",  # nord9
    comment="#5E81AC",  # nord10
    cycle=[
        "#88C0D0",  # nord8, blue
        "#D08770",  # nord12, orange
        "#A3BE8C",  # nord14, green
        "#BF616A",  # nord11, red
        "#B48EAD",  # nord15, purple
        # "",  # pink
        # "",  # gray
        "#EBCB8B",  # nord13, yellow
    ],
)
