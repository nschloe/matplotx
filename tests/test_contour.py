import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

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


def test_contours():
    def rosenbrock(x):
        return (1.0 - x[0]) ** 2 + 100.0 * (x[1] - x[0] ** 2) ** 2

    x = np.linspace(-3.0, 3.0, 200)
    y = np.linspace(-1.0, 3.0, 200)
    x, y = np.meshgrid(x, y)
    vals = rosenbrock(np.array([x, y]))
    plt.contourf(x, y, vals, locator=ticker.LogLocator())
    plt.gca().set_aspect("equal")
    # plt.savefig("mpl-contourf.svg", transparent=True, bbox_inches="tight")
    plt.show()
    plt.close()

    matplotx.contours(
        rosenbrock,
        (-3.0, 3.0, 200),
        (-1.0, 3.0, 200),
        log_scaling=True,
        cmap="viridis",
        outline="white",
    )
    plt.gca().set_aspect("equal")
    # plt.colorbar(im)
    # plt.savefig("matplotx-contours.svg", transparent=True, bbox_inches="tight")
    plt.show()
    plt.close()


if __name__ == "__main__":
    test_contours()
