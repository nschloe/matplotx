from __future__ import annotations

import matplotlib as mpl
from matplotlib.colors import to_rgb


# https://stackoverflow.com/a/26853961/353337
def _merge(dict1, dict2):
    """Merge two dicts, dict2 takes precedence."""
    return {**dict1, **dict2}


def duftify(style: dict, bar: bool = False) -> dict:
    from colorio.cs import OKLAB, SRGB1, ColorCoordinates, SRGBhex

    foreground = style["text.color"] if "text.color" in style else "black"
    background = style["figure.facecolor"] if "figure.facecolor" in style else "white"

    # perform interpolation in OKLAB
    foreground = ColorCoordinates(to_rgb(foreground), SRGB1())
    background = ColorCoordinates(to_rgb(background), SRGB1())
    foreground.convert(OKLAB())
    background.convert(OKLAB())
    t = 0.5
    pale = foreground * t + background * (1 - t)
    # convert back to SRGB hex
    pale.convert(SRGBhex(mode="clip", prepend=""))
    pale = pale.data.item()

    _stroke_width = 0.3
    # make the xticks slightly wider to make them easier to see
    _xtick_width = 0.4

    # See <https://matplotlib.org/stable/tutorials/introductory/customizing.html> for all
    # possible rcParams.
    dufte_style = {
        "font.size": 14,
        "text.color": pale,
        "axes.labelcolor": pale,
        "axes.labelpad": 18,
        "axes.spines.left": False,
        "axes.spines.bottom": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "ytick.minor.left": False,
        # Axes aren't used in this theme, but still set some properties in case the user
        # decides to turn them on.
        "axes.edgecolor": pale,
        "axes.linewidth": _stroke_width,
        # default is "line", i.e., below lines but above patches (bars)
        "axes.axisbelow": True,
        #
        "ytick.right": False,
        "ytick.color": pale,
        "ytick.major.width": _stroke_width,
        "xtick.minor.top": False,
        "xtick.minor.bottom": False,
        "xtick.color": pale,
        "xtick.major.width": _xtick_width,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": pale,
        # Choose the line width such that it's very subtle, but still serves as a guide.
        "grid.linewidth": _stroke_width,
        "axes.xmargin": 0,
        "axes.ymargin": 0,
        "axes.titlepad": 40,
        "axes.titlesize": 14,
    }

    if bar:
        # hide xticks for bars; the label is enough
        dufte_style["xtick.major.width"] = 0
        # unhide the bar labels
        dufte_style["xtick.major.pad"] = 13
        dufte_style["font.size"] = 16
        # default:
        dufte_style["axes.xmargin"] = mpl.rcParams["axes.xmargin"]
        # style_bar["ytick.major.size"] = 10
        dufte_style["axes.titlelocation"] = "left"
        dufte_style["axes.titlesize"] = 18

    return _merge(style, dufte_style)


dufte = duftify({})
dufte_bar = duftify({}, bar=True)
