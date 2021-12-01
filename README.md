# mplx

Some useful extensions for [Matplotlib](https://matplotlib.org/).

[![PyPi Version](https://img.shields.io/pypi/v/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/mplx.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/mplx)
[![Downloads](https://pepy.tech/badge/mplx/month)](https://pepy.tech/project/mplx)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/mplx/ci?style=flat-square)](https://github.com/nschloe/mplx/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/mplx.svg?style=flat-square)](https://codecov.io/gh/nschloe/mplx)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/mplx.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/mplx)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

### Extra styles

mplx contains numerous extra color schemes, e.g.,
[Dracula](https://draculatheme.com/), [Nord](https://www.nordtheme.com/),
[gruvbox](https://github.com/morhetz/gruvbox), and
[Solarized](https://ethanschoonover.com/solarized/).

<!--pytest-codeblocks:skip-->

```python
import matplotlib.pyplot as plt
import mplx

with plt.style.context(mplx.styles.dracula):
    # create figure
    pass
```

|    <img src="https://nschloe.github.io/mplx/aura-dark-soft.svg" width="100%">     |
| :-------------------------------------------------------------------------------: |
|       <img src="https://nschloe.github.io/mplx/aura-dark.svg" width="100%">       |
|       <img src="https://nschloe.github.io/mplx/ayu-dark.svg" width="100%">        |
|       <img src="https://nschloe.github.io/mplx/ayu-light.svg" width="100%">       |
|      <img src="https://nschloe.github.io/mplx/ayu-mirage.svg" width="100%">       |
|    <img src="https://nschloe.github.io/mplx/challenger-deep.svg" width="100%">    |
|        <img src="https://nschloe.github.io/mplx/dracula.svg" width="100%">        |
|     <img src="https://nschloe.github.io/mplx/gruvbox-dark.svg" width="100%">      |
|     <img src="https://nschloe.github.io/mplx/gruvbox-light.svg" width="100%">     |
|         <img src="https://nschloe.github.io/mplx/nord.svg" width="100%">          |
|       <img src="https://nschloe.github.io/mplx/one-dark.svg" width="100%">        |
|        <img src="https://nschloe.github.io/mplx/pacoty.svg" width="100%">         |
| <img src="https://nschloe.github.io/mplx/pitaya-smoothie-dark.svg" width="100%">  |
| <img src="https://nschloe.github.io/mplx/pitaya-smoothie-light.svg" width="100%"> |
|    <img src="https://nschloe.github.io/mplx/solarized-dark.svg" width="100%">     |
|    <img src="https://nschloe.github.io/mplx/solarized-light.svg" width="100%">    |
|    <img src="https://nschloe.github.io/mplx/tokyo-night-day.svg" width="100%">    |
|   <img src="https://nschloe.github.io/mplx/tokyo-night-night.svg" width="100%">   |
|   <img src="https://nschloe.github.io/mplx/tokyo-night-storm.svg" width="100%">   |

### Contour plots for functions with discontinuities

| <img src="https://nschloe.github.io/mplx/contour-mpl.svg" width="100%"> | <img src="https://nschloe.github.io/mplx/contour-mplx.svg" width="100%"> |
| :---------------------------------------------------------------------: | :----------------------------------------------------------------------: |
|                              `plt.contour`                              |                       `mplx.contour(max_jump=1.0)`                       |

Matplotlib has problems with contour plots of functions that have discontinuities. The
software has no way to tell discontinuities and very sharp, but continuous cliffs apart,
and contour lines will be drawn along the discontinuity.

mplx improves upon this by adding the parameter `max_jump`. If the difference between
two function values in the grid is larger than `max_jump`, a discontinuity is assumed
and no line is drawn. Similarly, `min_jump` can be used to highlight the discontinuity.

As an example, take the function `imag(log(Z))` for complex values Z. Matplotlib's
contour lines along the negative real axis are wrong.

```python
import matplotlib.pyplot as plt
import numpy as np

import mplx

x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

vals = np.imag(np.log(Z))

# plt.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0])  # draws wrong lines

mplx.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0], max_jump=1.0)
mplx.discontour(X, Y, vals, min_jump=1.0, linestyle=":", color="r")

plt.gca().set_aspect("equal")
plt.show()
```

Relevant discussions:

- [matplotlib/issues/21348](https://github.com/matplotlib/matplotlib/issues/21348)

### License

This software is published under the [MIT license](LICENSE).
