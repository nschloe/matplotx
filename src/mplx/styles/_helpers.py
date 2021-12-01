import matplotlib as mpl


def generate_style(foreground, background, cycle):
    return {
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
        "axes.prop_cycle": mpl.cycler(color=cycle),
    }
