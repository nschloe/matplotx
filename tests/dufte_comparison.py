import matplotlib.pyplot as plt
import numpy as np

import matplotx


def line():
    rng = np.random.default_rng(0)

    offsets = [1.0, 1.50, 1.60]
    labels = ["no balancing", "CRV-27", "CRV-27*"]
    x0 = np.linspace(0.0, 3.0, 100)
    y = [offset * x0 / (x0 + 1) + 0.1 * rng.random(len(x0)) for offset in offsets]

    # default mpl
    with plt.style.context("default"):
        for yy, label in zip(y, labels):
            plt.plot(x0, yy, label=label)
        plt.xlabel("distance [m]")
        plt.ylabel("voltage [V]")
        plt.legend()
        plt.savefig("ex1-mpl.svg", bbox_inches="tight")
        plt.close()

    # dufte
    with plt.style.context(matplotx.styles.dufte):
        for yy, label in zip(y, labels):
            plt.plot(x0, yy, label=label)
        plt.xlabel("distance [m]")
        matplotx.ylabel_top("voltage [V]")
        matplotx.line_labels()
        plt.savefig("ex1-dufte.svg", bbox_inches="tight")
        plt.close()

    # dufte
    with plt.style.context(matplotx.styles.duftify(matplotx.styles.dracula)):
        for yy, label in zip(y, labels):
            plt.plot(x0, yy, label=label)
        plt.xlabel("distance [m]")
        matplotx.ylabel_top("voltage [V]")
        matplotx.line_labels()
        plt.savefig("ex1-dufte-dracula.svg", bbox_inches="tight")
        plt.close()


def bars():
    labels = ["Australia", "Brazil", "China", "Germany", "Mexico", "United\nStates"]
    vals = [21.65, 24.5, 6.95, 8.40, 21.00, 8.55]
    xpos = range(len(vals))

    with plt.style.context("default"):
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        plt.title("average temperature [°C]")
        plt.savefig("bars-mpl.svg", transparent=True, bbox_inches="tight")
        plt.close()

    with plt.style.context(matplotx.styles.dufte_bar):
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        plt.title("average temperature [°C]")
        plt.savefig("bars-dufte1.svg", transparent=True, bbox_inches="tight")
        plt.close()

    with plt.style.context(matplotx.styles.dufte_bar):
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        matplotx.show_bar_values("{:.2f}")
        plt.title("average temperature [°C]")
        plt.savefig("bars-dufte2.svg", transparent=True, bbox_inches="tight")
        plt.close()


if __name__ == "__main__":
    line()
    bars()
