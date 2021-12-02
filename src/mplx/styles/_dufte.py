import matplotlib as mpl

# The CIELAB average between GitHub's dark and light font is #71777e. This is hard to
# read on dark background, though, and a little too dark on light background, too. Make
# it lighter. The color #969696 appears to strike a good balance.
_gray = "969696"
_stroke_width = 0.3
# make the xticks slightly wider to make them easier to see
_xtick_width = 0.4

# See <https://matplotlib.org/stable/tutorials/introductory/customizing.html> for all
# possible rcParams.
dufte = {
    "font.size": 14,
    "text.color": _gray,
    "axes.labelcolor": _gray,
    "axes.labelpad": 18,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "ytick.minor.left": False,
    # Axes aren't used in this theme, but still set some properties in case the user
    # decides to turn them on.
    "axes.edgecolor": _gray,
    "axes.linewidth": _stroke_width,
    # default is "line", i.e., below lines but above patches (bars)
    "axes.axisbelow": True,
    #
    "ytick.right": False,
    "ytick.color": _gray,
    "ytick.major.width": _stroke_width,
    "xtick.minor.top": False,
    "xtick.minor.bottom": False,
    "xtick.color": _gray,
    "xtick.major.width": _xtick_width,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": _gray,
    # Choose the line width such that it's very subtle, but still serves as a guide.
    "grid.linewidth": _stroke_width,
    "axes.xmargin": 0,
    "axes.ymargin": 0,
    "axes.titlepad": 40,
    "axes.titlesize": 14,
}

dufte_bar = dufte.copy()
# hide xticks for bars; the label is enough
dufte_bar["xtick.major.width"] = 0
# unhide the bar labels
dufte_bar["xtick.major.pad"] = 13
dufte_bar["font.size"] = 16
# default:
dufte_bar["axes.xmargin"] = mpl.rcParams["axes.xmargin"]
# style_bar["ytick.major.size"] = 10
dufte_bar["axes.titlelocation"] = "left"
dufte_bar["axes.titlesize"] = 18
