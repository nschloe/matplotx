import numpy


def nnls(A, b, eps: float = 1.0e-10, max_steps: int = 100):
    # non-negative least-squares after
    # <https://en.wikipedia.org/wiki/Non-negative_least_squares>
    A = numpy.asarray(A)
    b = numpy.asarray(b)

    AtA = A.T @ A
    Atb = A.T @ b

    m, n = A.shape
    assert m == b.shape[0]
    mask = numpy.zeros(n, dtype=bool)
    x = numpy.zeros(n)
    w = Atb
    s = numpy.zeros(n)
    k = 0
    while sum(mask) != n and max(w) > eps:
        if k >= max_steps:
            break
        mask[numpy.argmax(w)] = True

        s[mask] = numpy.linalg.lstsq(AtA[mask][:, mask], Atb[mask], rcond=None)[0]
        s[~mask] = 0.0

        while numpy.min(s[mask]) <= 0:
            alpha = numpy.min(x[mask] / (x[mask] - s[mask]))
            x += alpha * (s - x)
            mask[numpy.abs(x) < eps] = False

            s[mask] = numpy.linalg.lstsq(AtA[mask][:, mask], Atb[mask], rcond=None)[0]
            s[~mask] = 0.0

        x = s.copy()
        w = Atb - AtA @ x

        k += 1

    return x
