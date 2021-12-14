from __future__ import annotations

import matplotlib as mpl
from matplotlib.colors import to_rgb


# https://stackoverflow.com/a/26853961/353337
def _merge(dict1, dict2):
    """Merge two dicts, dict2 takes precedence."""
    return {**dict1, **dict2}


def duftify(style: dict, bar: bool = False) -> dict:
    from colorio.cs import OKLAB, SRGB1, ColorCoordinates, SRGBhex

    foreground = style["text.color"]
    background = style["figure.facecolor"]

    # If it's a hex number, prepend "#"
    try:
        int(foreground, 16)
    except ValueError:
        pass
    else:
        foreground = "#" + foreground

    try:
        int(background, 16)
    except ValueError:
        pass
    else:
        background = "#" + background

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

    # See <https://matplotlib.org/stable/tutorials/introductory/customizing.html> for all
    # possible rcParams.
    out = _merge(style, dufte_style)

    # mpl.rcParamsDefault contains many keys that give a UserWarning,
    # ```
    # UserWarning: Style includes a parameter, 'backend', that is not related
    # to style.  Ignoring this parameter.
    # ```
    # Remove those.
    rm_keys = [
        "backend_fallback",
        "date.epoch",
        "docstring.hardcopy",
        "figure.max_open_warning",
        "figure.raise_window",
        "backend",
        "interactive",
        "savefig.directory",
        "timezone",
        "tk.window_focus",
        "toolbar",
        "webagg.address",
        "webagg.open_in_browser",
        "webagg.port",
        "webagg.port_retries",
    ]

    for key in rm_keys:
        if key in out:
            out.pop(key)

    return out


dufte = duftify(mpl.rcParamsDefault.copy())
dufte_bar = duftify(mpl.rcParamsDefault.copy(), bar=True)
