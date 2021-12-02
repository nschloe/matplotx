import matplotlib.pyplot as plt
import numpy as np

import matplotx


def test_plot():
    offsets = [1.0, 1.50, 1.60]
    offsets = [1.0, 1.50, 1.51]

    x0 = np.linspace(0.0, 3.0, 100)
    labels = ["no balancing", "CRV-27", "CRV-27*"]

    with plt.style.context(matplotx.styles.dufte):
        for label, offset in zip(labels, offsets):
            y0 = offset * x0 / (x0 + 1)
            plt.plot(x0, y0, label=label)

        plt.xlabel("distance [m]")
        matplotx.ylabel_top("voltage [V]")
        # plt.title("title")
        matplotx.line_labels()


def test_no_labels():
    plt.style.use(matplotx.styles.dufte)

    np.random.seed(0)
    n = 100
    x0 = np.linspace(0.0, 3.0, n)
    y0 = 1.0 + 0.1 * np.random.rand(n)
    plt.plot(x0, y0, label="rand 1")

    y0 = 2.0 + 0.1 * np.random.rand(n)
    # no label
    plt.plot(x0, y0)

    y0 = 3.0 + 0.1 * np.random.rand(n)
    plt.plot(x0, y0, label="rand 3")

    matplotx.line_labels()
    # plt.legend()
    plt.show()


def test_nan():
    plt.style.use(matplotx.styles.dufte)
    x0 = [0.0, 0.5, 1.0]
    y0 = [0.0, 0.5, np.nan]
    plt.plot(x0, y0, label="nan")

    matplotx.line_labels()
    # plt.legend()
    plt.show()


def test_all_nan():
    plt.style.use(matplotx.styles.dufte)
    x0 = [0.0, 0.5, 1.0]
    y0 = [np.nan, np.nan, np.nan]
    plt.plot(x0, y0, label="nan")

    matplotx.line_labels()
    # plt.legend()
    plt.show()


def test_logy():
    plt.style.use(matplotx.styles.dufte)
    x0 = [0.0, 0.5, 1.0, 10.0]
    y0 = np.exp(x0)
    plt.semilogy(x0, y0, label="exp")
    matplotx.line_labels()
    matplotx.ylabel_top("ylabel")


if __name__ == "__main__":
    test_logy()
    plt.show()
    plt.close()
