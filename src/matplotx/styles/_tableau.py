"""
The tableau colors have been revised in [1], but it's unclear where they can be
used (see [2]). Hence, just provide a reordering of the tab20 colors that are in matplotlib.

[1] https://www.tableau.com/about/blog/2016/7/colors-upgrade-tableau-10-56782
[2] https://jrnold.github.io/ggthemes/reference/tableau_color_pal.html
"""
import matplotlib as mpl


def _flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def _transpose(list_of_lists):
    return list(map(list, zip(*list_of_lists)))


tab20_colors = [
    ["1f77b4", "aec7e8"],  # blue
    ["ff7f0e", "ffbb78"],  # orange
    ["2ca02c", "98df8a"],  # green
    ["d62728", "ff9896"],  # red
    ["9467bd", "c5b0d5"],  # purple
    ["8c564b", "c49c94"],  # brown
    ["e377c2", "f7b6d2"],  # pink
    ["7f7f7f", "c7c7c7"],  # gray
    ["bcbd22", "dbdb8d"],  # yellow
    ["17becf", "9edae5"],  # teal
]
tab10 = {"axes.prop_cycle": mpl.cycler(color=[row[0] for row in tab20_colors])}
tab20 = {"axes.prop_cycle": mpl.cycler(color=_flatten(tab20_colors))}
# like tab20, but reordered such that the light variants come last
tab20r = {"axes.prop_cycle": mpl.cycler(color=_flatten(_transpose(tab20_colors)))}
