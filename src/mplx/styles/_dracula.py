"""
https://draculatheme.com/
"""
import matplotlib as mpl

background = "282a36"
foreground = "f8f8f2"
comment = "6272a4"
cyan = "8be9fd"
green = "50fa7b"
orange = "ffb86c"
pink = "ff79c6"
purple = "bd93f9"
red = "ff5555"
yellow = "f1fa8c"

dracula = {
    "lines.color": foreground,
    "patch.edgecolor": foreground,
    "text.color": foreground,
    "axes.facecolor": background,
    "axes.edgecolor": foreground,
    "axes.labelcolor": foreground,
    "xtick.color": foreground,
    "ytick.color": foreground,
    "legend.framealpha": 0,
    "grid.color": foreground,
    "figure.facecolor": background,
    "figure.edgecolor": background,
    "savefig.facecolor": background,
    "savefig.edgecolor": background,
    "boxplot.boxprops.color": foreground,
    "boxplot.capprops.color": foreground,
    "boxplot.flierprops.color": foreground,
    "boxplot.flierprops.markeredgecolor": foreground,
    "boxplot.whiskerprops.color": foreground,
    "axes.prop_cycle": mpl.cycler(
        color=[
            # choose color order similar to tab10
            cyan,
            orange,
            green,
            red,
            purple,
            # brown
            pink,
            comment,
            yellow,
        ],
    )
}
