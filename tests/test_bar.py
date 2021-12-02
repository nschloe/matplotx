import matplotlib.pyplot as plt

import mplx


def test_bar():
    with plt.style.context(mplx.styles.dufte_bar):
        labels = ["label 1", "label 2"]
        vals = [2.1, 6.3]
        xpos = range(len(vals))
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        mplx.show_bar_values("{:.2f}")
        plt.title("some title")
        plt.close()


if __name__ == "__main__":
    test_bar()
    plt.show()
    plt.close()
