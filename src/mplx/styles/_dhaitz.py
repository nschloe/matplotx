"""
https://github.com/dhaitz/matplotlib-stylesheets
"""
import matplotlib as mpl


def _merge(x, y):
    # Python 3.9+: z = x | y
    return {**x, **y}


_base = {
    "legend.frameon": False,
    "legend.numpoints": 1,
    "legend.scatterpoints": 1,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "axes.axisbelow": True,
    "font.family": "sans-serif",
    "grid.linestyle": "-",
    "lines.solid_capstyle": "round",
    "axes.grid": True,
    "axes.linewidth": 0,
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "xtick.minor.size": 0,
    "ytick.minor.size": 0,
    "image.cmap": "RdPu",
}

pitaya_smoothie = {
    "light": _merge(
        _base,
        {
            "text.color": "0.15",
            "axes.labelcolor": "0.15",
            "xtick.color": "0.15",
            "ytick.color": "0.15",
            "axes.facecolor": "EAEAF2",
            "axes.edgecolor": "white",
            "grid.color": "white",
            "axes.prop_cycle": mpl.cycler(
                color=["7A76C2", "ff6e9c98", "f62196", "18c0c4", "f3907e", "66E9EC"]
            ),
            "figure.facecolor": "fefeff",
            "savefig.facecolor": "fefeff",
        },
    ),
    "dark": _merge(
        _base,
        {
            "text.color": "0.9",
            "axes.labelcolor": "0.9",
            "xtick.color": "0.9",
            "ytick.color": "0.9",
            "axes.facecolor": "212946",
            "axes.edgecolor": "white",
            "grid.color": "2A3459",
            "axes.prop_cycle": mpl.cycler(
                color=["18c0c4", "f62196", "A267F5", "f3907e", "ffe46b", "fefeff"]
            ),
            "figure.facecolor": "212946",
            "savefig.facecolor": "212946",
        },
    ),
}


pacoty = _merge(
    _base,
    {
        "text.color": ".15",
        "axes.labelcolor": ".15",
        "xtick.color": ".15",
        "ytick.color": ".15",
        "axes.facecolor": "EAEAF2",
        "axes.edgecolor": "white",
        "grid.color": "white",
        "axes.prop_cycle": mpl.cycler(
            color=["5A5B9F", "D94F70", "009473", "F0C05A", "7BC4C4", "FF6F61"],
        ),
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    },
)
