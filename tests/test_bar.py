import matplotlib.pyplot as plt
import pytest

import matplotx


def test_bar():
    with plt.style.context(matplotx.styles.dufte_bar):
        labels = ["label 1", "label 2"]
        vals = [2.1, 6.3]
        xpos = range(len(vals))
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        matplotx.show_bar_values("{:.2f}")
        plt.title("some title")
        plt.close()


def test_bar_horizontal():
    """Checks that a bar chart can be created with horizontal alignment"""
    with plt.style.context(matplotx.styles.dufte_bar):
        labels = ["label 1", "label 2"]
        vals = [2.1, 6.3]
        ypos = range(len(vals))
        plt.barh(ypos, vals)
        plt.xticks(ypos, labels)
        matplotx.show_bar_values("{:.2f}", alignment="horizontal")
        plt.title("some title")
        plt.close()


def test_wrong_alignment():
    """Checks that an error is raised when alignment has an invalid value"""
    with pytest.raises(ValueError, match="Unknown alignment"):
        matplotx.show_bar_values(alignment="coucou")


if __name__ == "__main__":
    test_bar()
    plt.show()
    plt.close()
