# mplx

[![PyPi Version](https://img.shields.io/pypi/v/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/mplx.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/mplx)
[![PyPi downloads](https://img.shields.io/pypi/dm/mplx.svg?style=flat-square)](https://pypistats.org/packages/mplx)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/mplx/ci?style=flat-square)](https://github.com/nschloe/mplx/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/mplx.svg?style=flat-square)](https://codecov.io/gh/nschloe/mplx)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/mplx.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/mplx)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

### Contour plots for functions with discontinuities

| <img src="https://nschloe.github.io/mplx/contour-mpl.svg" width="100%"> | <img src="https://nschloe.github.io/mplx/contour-mplx.svg" width="100%"> |
| :---------------------------------------------------------------------: | :----------------------------------------------------------------------: |
|                              `plt.contour`                              |                       `mplx.contour(max_jump=1.0)                        |


```python
import matplotlib.pyplot as plt
import numpy as np

import mplx

x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

vals = np.imag(np.log(Z))

# plt.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0])
mplx.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0], max_jump=1.0)
mplx.contour(X, Y, vals, levels=[0.0], min_jump=1.0, linestyles=":")

plt.gca().set_aspect("equal")
plt.show()
```

### License

This software is published under the [MIT license](LICENSE).
