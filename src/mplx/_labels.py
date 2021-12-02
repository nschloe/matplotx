from __future__ import annotations

import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import ArrayLike

from ._optimize import nnls


def _move_min_distance(targets: ArrayLike, min_distance: float) -> np.ndarray:
    """Move the targets such that they are close to their original positions, but keep
    min_distance apart.

    https://math.stackexchange.com/a/3705240/36678
    """
    # sort targets
    idx = np.argsort(targets)
    targets = np.sort(targets)

    n = len(targets)
    x0_min = targets[0] - n * min_distance
    A = np.tril(np.ones([n, n]))
    b = targets - (x0_min + np.arange(n) * min_distance)

    # import scipy.optimize
    # out, _ = scipy.optimize.nnls(A, b)

    out = nnls(A, b)

    sol = np.cumsum(out) + x0_min + np.arange(n) * min_distance

    # reorder
    idx2 = np.argsort(idx)
    return sol[idx2]


def line_labels(ax=None, min_label_distance: float | str = "auto", alpha: float = 1.0):
    ax = ax or plt.gca()

    logy = ax.get_yscale() == "log"

    if min_label_distance == "auto":
        # Make sure that the distance is alpha * fontsize. This needs to be translated
        # into axes units.
        fig = plt.gcf()
        fig_height_inches = fig.get_size_inches()[1]
        ax = plt.gca()
        ax_pos = ax.get_position()
        ax_height = ax_pos.y1 - ax_pos.y0
        ax_height_inches = ax_height * fig_height_inches
        ylim = ax.get_ylim()
        if logy:
            print(ylim)
            ax_height_ylim = math.log10(ylim[1]) - math.log10(ylim[0])
        else:
            ax_height_ylim = ylim[1] - ylim[0]
        # 1 pt = 1/72 in
        fontsize = mpl.rcParams["font.size"]
        assert fontsize is not None
        min_label_distance_inches = fontsize / 72 * alpha
        min_label_distance = (
            min_label_distance_inches / ax_height_inches * ax_height_ylim
        )

    # find all Line2D objects with a valid label and valid data
    lines = [
        child
        for child in ax.get_children()
        # https://stackoverflow.com/q/64358117/353337
        if (
            isinstance(child, mpl.lines.Line2D)
            and child.get_label()[0] != "_"
            and not np.all(np.isnan(child.get_ydata()))
        )
    ]

    if len(lines) == 0:
        return

    # Add "legend" entries.
    # Get last non-nan y-value.
    targets = []
    for line in lines:
        ydata = line.get_ydata()
        targets.append(ydata[~np.isnan(ydata)][-1])

    if logy:
        targets = [math.log10(t) for t in targets]

    # Sometimes, the max value if beyond ymax. It'd be cool if in this case we could put
    # the label above the graph (instead of the to the right), but for now let's just
    # cap the target y.
    ymax = ax.get_ylim()[1]
    targets = [min(target, ymax) for target in targets]

    targets = _move_min_distance(targets, min_label_distance)
    if logy:
        targets = [10 ** t for t in targets]

    labels = [line.get_label() for line in lines]
    colors = [line.get_color() for line in lines]

    # Leave the labels some space to breathe. If they are too close to the
    # lines, they can get visually merged.
    # <https://twitter.com/EdwardTufte/status/1416035189843714050>
    # Don't forget to transform to axis coordinates first. This makes sure the
    # https://stackoverflow.com/a/40475221/353337
    axis_to_data = ax.transAxes + ax.transData.inverted()
    xpos = axis_to_data.transform([1.03, 1.0])[0]
    for label, ypos, color in zip(labels, targets, colors):
        plt.text(xpos, ypos, label, verticalalignment="center", color=color)


def ylabel_top(string: str) -> None:
    # Rotate the ylabel (such that you can read it comfortably) and place it above the
    # top ytick. This requires some logic, so it cannot be incorporated in `style`.
    # See <https://stackoverflow.com/a/27919217/353337> on how to get the axes
    # coordinates of the top ytick.
    ax = plt.gca()

    yticks_pos = ax.get_yticks()
    coords = np.column_stack([np.zeros_like(yticks_pos), yticks_pos])
    data_to_axis = ax.transData + ax.transAxes.inverted()
    yticks_pos_ax = data_to_axis.transform(coords)[:, 1]
    # filter out the ticks which aren't shown
    tol = 1.0e-5
    yticks_pos_ax = yticks_pos_ax[(-tol < yticks_pos_ax) & (yticks_pos_ax < 1.0 + tol)]
    if len(yticks_pos_ax) > 0:
        pos_y = yticks_pos_ax[-1] + 0.1
    else:
        pos_y = 1.0

    # Get the padding in axes coordinates. The below logic isn't quite correct, so keep
    # an eye on <https://stackoverflow.com/q/67872207/353337> and
    # <https://discourse.matplotlib.org/t/get-ytick-label-distance-in-axis-coordinates/22210>
    # and
    # <https://github.com/matplotlib/matplotlib/issues/20677>
    yticks = ax.yaxis.get_major_ticks()
    if len(yticks) == 0:
        pos_x = 0.0
    else:
        pad_pt = yticks[-1].get_pad()
        # https://stackoverflow.com/a/51213884/353337
        # ticklen_pt = ax.yaxis.majorTicks[0].tick1line.get_markersize()
        # dist_in = (pad_pt + ticklen_pt) / 72.0
        dist_in = pad_pt / 72.0
        # get axes width in inches
        # https://stackoverflow.com/a/19306776/353337
        bbox = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
        pos_x = -dist_in / bbox.width

    yl = plt.ylabel(string, horizontalalignment="right", multialignment="right")
    # place the label 10% above the top tick
    ax.yaxis.set_label_coords(pos_x, pos_y)
    yl.set_rotation(0)


def show_bar_values(fmt: str = "{}") -> None:
    ax = plt.gca()

    # turn off y-ticks and y-grid
    plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
    plt.grid(False)

    # remove margins
    plt.margins(x=0)

    data_to_axis = ax.transData + ax.transAxes.inverted()
    axis_to_data = ax.transAxes + ax.transData.inverted()

    for rect in ax.patches:
        height = rect.get_height()
        ypos_ax = data_to_axis.transform([1.0, height])
        ypos = axis_to_data.transform(ypos_ax - 0.1)[1]
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            ypos,
            fmt.format(height),
            size=14,
            weight="bold",
            ha="center",
            va="bottom",
            color="white",
        )
