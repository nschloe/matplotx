"""
Color data as hand-taken from GitHub.
"""
from ._helpers import generate_style

github = {
    "light": generate_style(
        background="ffffff",
        foreground="24292f",
        cycle=[
            "0550ae",  # blue
            "953800",  # orange
            "116329",  # green
            "cf222e",  # red
            "8250df",  # purple
            "6e7781",  # gray
        ],
    ),
    "dark": generate_style(
        background="161b22",
        foreground="f0f6fc",
        cycle=[
            "79c0ff",  # blue
            "ffa657",  # orange
            "7ee787",  # green
            "ff7b72",  # red
            "d2a8ff",  # purple
            "8b949e",  # gray
        ],
    ),
    "dimmed": generate_style(
        background="22272e",
        foreground="adbac7",
        cycle=[
            "6cb6ff",  # blue
            "f69d50",  # orange
            "8ddb8c",  # green
            "f47067",  # red
            "dcbdfb",  # purple
            "768390",  # gray
        ],
    ),
}
