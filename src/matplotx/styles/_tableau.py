"""
https://www.tableau.com/about/blog/2016/7/colors-upgrade-tableau-10-56782
https://jrnold.github.io/ggthemes/reference/tableau_color_pal.html
"""
import matplotlib as mpl


def _flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def _transpose(list_of_lists):
    return list(map(list, zip(*list_of_lists)))


tab10 = {
    "axes.prop_cycle": mpl.cycler(
        color=[
            "4e79a7",  # blue
            "f28e2b",  # orange
            "e15759",  # red
            "76b7b2",  # teal
            "59a14f",  # green
            "edc948",  # yellow
            "b07aa1",  # purple
            "ff9da7",  # rose
            "9c755f",  # brown
            "bab0ac",  # grey
        ]
    ),
}

# colors plus light variant; some are the same as tab10
tab20_colors = [
    ["4e79a7", "a0cbe8"],  # blue
    ["f28e2b", "ffbe7d"],  # orange
    ["59a14f", "8cd17d"],  # green
    ["b6992d", "f1ce63"],  # yellow
    ["499894", "86bcb6"],  # teal
    ["e15759", "ff9d9a"],  # red
    ["79706e", "bab0ac"],  # grey
    ["d37295", "fabfd2"],  # rose
    ["b07aa1", "d4a6c8"],  # purple
    ["9c7660", "d7b5a6"],  # brown
]
tab20 = {"axes.prop_cycle": mpl.cycler(color=_flatten(tab20_colors))}
# like tab20, but reordered such that the light variants come last
tab20r = {"axes.prop_cycle": mpl.cycler(color=_flatten(_transpose(tab20_colors)))}
