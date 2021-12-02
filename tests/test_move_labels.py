import pytest

import matplotx


def assert_equality(a, b, eps):
    for x, y in zip(a, b):
        assert abs(x - y) < eps


@pytest.mark.parametrize(
    "pos, dist, ref",
    [
        ([0.0, 1.0], 2.0, [-0.5, 1.5]),
        ([0.0, 1.0, 3.0], 2.0, [-2 / 3, 4 / 3, 10 / 3]),
        ([0.0, 0.0, 3.0], 2.0, [-1.0, 1.0, 3.0]),
    ],
)
def test_move_labels(pos, dist, ref):
    out = matplotx._labels._move_min_distance(pos, dist)
    assert_equality(out, ref, 1.0e-5)
