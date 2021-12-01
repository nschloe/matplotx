"""
https://github.com/daltonmenezes/aura-theme
https://github.com/daltonmenezes/aura-theme/tree/main/packages/color-palettes
"""
from ._helpers import generate_style

aura = {
    "dark": generate_style(
        background="15141b",
        foreground="edecee",
        cycle=[
            "82e2ff",  # blue
            "ffca85",  # orange
            "61ffca",  # green
            "ff6767",  # red
            "a277ff",  # purple
            "f694ff",  # magenta
            "6d6d6d",  # gray
        ],
    ),
    "dark-soft": generate_style(
        background="15141b",
        foreground="bdbdbd",
        cycle=[
            "6cb2c7",  # blue
            "c7a06f",  # orange
            "54c59f",  # green
            "c55858",  # red
            "8464c6",  # purple
            "c17ac8",  # magenta
            "6d6d6d",  # gray
        ],
    ),
}
