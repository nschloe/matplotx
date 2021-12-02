"""
https://draculatheme.com/
"""
from ._helpers import generate_style

dracula = generate_style(
    foreground="f8f8f2",
    background="282a36",
    # choose color order similar to tab10
    cycle=[
        "8be9fd",  # cyan
        "ffb86c",  # orange
        "50fa7b",  # green
        "ff5555",  # red
        "bd93f9",  # purple
        "ff79c6",  # pink
        "6272a4",  # comment
        "f1fa8c",  # yellow
    ],
)
