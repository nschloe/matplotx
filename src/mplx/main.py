from __future__ import annotations

import matplotlib.pyplot as plt
import networkx
import numpy as np
from numpy.typing import ArrayLike


def contour(
    X: ArrayLike,
    Y: ArrayLike,
    Z: ArrayLike,
    levels: list[float],
    min_jump: float | None = None,
    max_jump: float | None = None,
    colors: str | list[str] | None = None,
    linestyles: str | None = None,
    alpha: float | None = None,
):
    X = np.asarray(X)
    Y = np.asarray(Y)
    Z = np.asarray(Z)

    # make sure that X, Y, Z are meshgrid-like
    assert len(X.shape) == 2
    assert X.shape == Y.shape
    assert X.shape == Z.shape
    assert np.all(X[0] == X)
    assert np.all(Y[:, 0] == Y.T)

    # transform the input data; this way it's easier to reason about
    x = X[0]
    y = Y[:, 0]
    Z = Z.T

    if isinstance(colors, str) or colors is None:
        colors = [colors] * len(levels)

    assert len(colors) == len(levels)

    for level, color in zip(levels, colors):
        # for each quad, check if the contour passes through it
        is_below = Z < level
        is_above = ~is_below  # Z > level

        # horizontal and vertical edges
        # horiz.shape = (nx - 1, ny)
        # verti.shape = (nx, ny - 1)
        horiz = ~np.logical_xor(is_below[:-1, :], is_above[1:, :])
        verti = ~np.logical_xor(is_below[:, :-1], is_above[:, 1:])
        if min_jump is not None:
            horiz &= np.abs(Z[:-1, :] - Z[1:, :]) > min_jump
            verti &= np.abs(Z[:, :-1] - Z[:, 1:]) > min_jump
        if max_jump is not None:
            horiz &= np.abs(Z[:-1, :] - Z[1:, :]) < max_jump
            verti &= np.abs(Z[:, :-1] - Z[:, 1:]) < max_jump

        G = networkx.Graph()

        bottom = horiz[:, :-1]
        top = horiz[:, 1:]
        left = verti[:-1, :]
        right = verti[1:, :]

        # quad k has edge ids as follows:
        #
        #            (2,i,j+1)
        #          +-----------+
        #          |           |
        #          |           |
        #  (1,i,j) |  (0,i,j)  | (1,i+1,j)
        #          |           |
        #          |           |
        #          +-----------+
        #             (2,i,j)
        #
        # `2` is for `is_horizontal`, `1` is for `is_vertical`, `0` is for quad center.
        # i[+1] and j[+1] are the indices in the horizontal or vertical array of edges.
        #
        # ONE edge -- connect edge and quad center
        quad_ij = np.array(np.where(bottom & ~left & ~top & ~right)).T
        id_pairs = [((2, i, j), (0, i, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & left & ~top & ~right)).T
        id_pairs = [((1, i, j), (0, i, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & ~left & top & ~right)).T
        id_pairs = [((2, i, j + 1), (0, i, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & ~left & ~top & right)).T
        id_pairs = [((1, i + 1, j), (0, i, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        # TWO edges -- connect two edges
        quad_ij = np.array(np.where(bottom & left & ~top & ~right)).T
        id_pairs = [((2, i, j), (1, i, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(bottom & ~left & top & ~right)).T
        id_pairs = [((2, i, j), (2, i, j + 1)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(bottom & ~left & ~top & right)).T
        id_pairs = [((2, i, j), (1, i + 1, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & left & top & ~right)).T
        id_pairs = [((1, i, j), (2, i, j + 1)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & left & ~top & right)).T
        id_pairs = [((1, i, j), (1, i + 1, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        #
        quad_ij = np.array(np.where(~bottom & ~left & top & right)).T
        id_pairs = [((2, i, j + 1), (1, i + 1, j)) for i, j in quad_ij]
        G.add_edges_from(id_pairs)
        # THREE edges TODO
        # FOUR edges TODO

        # find odd-degree node to start with
        source = None
        for node, degree in G.degree:
            if degree % 2 == 1:
                source = node
                break

        # find edge covering,
        # https://github.com/networkx/networkx/discussions/5147
        T = networkx.algorithms.traversal.edgedfs.edge_dfs(G, source)
        T = list(T)
        T = np.asarray(T)

        is_domino_match = np.all(T[:-1, 1] == T[1:, 0], axis=1)
        split_idx = np.where(~is_domino_match)[0] + 1
        edge_paths = np.split(T, split_idx)
        node_paths = [np.concatenate([ep[:, 0], [ep[-1, 1]]]) for ep in edge_paths]

        # iterate over the paths, find the coordinates of the nodes, and plot
        Z_level = Z - level
        for path in node_paths:
            # translate the indices into coordinates
            node_type, i_, j_ = path.T
            x_, y_ = np.empty((2, len(path)))

            assert np.all((0 <= node_type) & (node_type <= 2))

            # nodes in quad centers
            is_center = node_type == 0
            i = i_[is_center]
            j = j_[is_center]
            x_[is_center] = (x[i] + x[i + 1]) / 2
            y_[is_center] = (y[j] + y[j + 1]) / 2

            # nodes on vertical edges
            is_vertical = node_type == 1
            i = i_[is_vertical]
            j = j_[is_vertical]
            # x stays the same
            x_[is_vertical] = x[i]
            # linear interpolation
            z_ij1 = Z_level[i, j + 1]
            z_ij = Z_level[i, j]
            y_[is_vertical] = (y[j] * z_ij1 - y[j + 1] * z_ij) / (z_ij1 - z_ij)

            # nodes on horizontal edges
            is_horizontal = node_type == 2
            i = i_[is_horizontal]
            j = j_[is_horizontal]
            # linear interpolation
            z_i1j = Z_level[i + 1, j]
            z_ij = Z_level[i, j]
            x_[is_horizontal] = (x[i] * z_i1j - x[i + 1] * z_ij) / (z_i1j - z_ij)
            # y stays the same
            y_[is_horizontal] = y[j]

            # finally, plot the contour
            plt.plot(x_, y_, linestyle=linestyles, color=color, alpha=alpha)

    return plt
