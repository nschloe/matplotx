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
                color=[
                    "7A76C2",  # purple
                    "f3907e",  # orange
                    "18c0c4",  # teal
                    "ff6e9c98",  # red
                    "66E9EC",  # light teal
                    "f62196",  # magenta
                ]
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
                color=[
                    "A267F5",  # purple
                    "f3907e",  # light orange
                    "18c0c4",  # teal
                    "f62196",  # magenta
                    "ffe46b",  # yellow
                    "fefeff",  # white
                ]
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
            color=[
                "5A5B9F",  # purple
                "FF6F61",  # orange
                "009473",  # green
                "D94F70",  # red
                "7BC4C4",  # teal
                "F0C05A",  # yellow
            ],
        ),
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    },
)
