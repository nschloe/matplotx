import matplotlib.pyplot as plt
import numpy as np

import matplotx


def test_plot():
    x = np.linspace(-1.0, 1.0, 10)
    y = np.linspace(-1.0, 1.0, 11)

    X, Y = np.meshgrid(x, y)

    z = X + 1j * Y
    vals = np.angle(z)

    # import time
    # t = time.time()
    # plt.contour(X, Y, vals, levels=[0.5], linestyles=":")
    # print("T", time.time() - t)
    # # plt.show()
    # t = time.time()
    # matplotx.contour(X, Y, vals, levels=[0.5], linestyles="-")
    # print("t", time.time() - t)

    matplotx.contour(X, Y, vals, levels=[0.5], max_jump=5.0)
    matplotx.discontour(X, Y, vals, min_jump=5.0, linestyle=":", color="r")
    plt.gca().set_aspect("equal")
    plt.show()
    plt.close()


def test_paths():
    x = np.linspace(-1.0, 1.0, 10)
    y = np.linspace(-1.0, 1.0, 11)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y
    vals = np.angle(z).T

    paths = matplotx._contour._get_xy_paths(
        x, y, vals, level=0.5, max_jump=5.0, min_jump=None
    )
    assert len(paths) == 1
    assert paths[0].shape == (2, 9)


def test_closed_path():
    delta = 0.5
    x = np.arange(-2.0, 2.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2) - Y**2)

    # plt.contour(X, Y, Z, levels=[0.75])
    matplotx.contour(X, Y, Z, levels=[0.75])
    plt.gca().set_aspect("equal")
    plt.show()
    plt.close()


def test_separate_paths():
    delta = 0.05
    x = np.arange(-2.0, 2.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-((X - 1) ** 2) - Y**2) + np.exp(-((X + 1) ** 2) - Y**2)

    # plt.contour(X, Y, Z, levels=[0.75])
    matplotx.contour(X, Y, Z, levels=[0.75])
    plt.gca().set_aspect("equal")
    plt.show()
    plt.close()


def test_multiple_levels():
    delta = 0.5
    x = np.arange(-2.0, 2.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2) - Y**2)

    # plt.contour(X, Y, Z, levels=[0.75])
    matplotx.contour(X, Y, Z, levels=[0.5, 0.75])
    plt.gca().set_aspect("equal")
    plt.show()
    plt.close()


if __name__ == "__main__":
    test_plot()
