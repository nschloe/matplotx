<p align="center">
  <a href="https://github.com/nschloe/mplx"><img alt="mplx" src="https://nschloe.github.io/mplx/mplx-logo.svg" width="55%"></a>
  <p align="center">Some useful extensions for <a href="https://matplotlib.org/">Matplotlib</a>.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mplx.svg?style=flat-square)](https://pypi.org/project/mplx/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/mplx.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/mplx)
[![Downloads](https://pepy.tech/badge/mplx/month)](https://pepy.tech/project/mplx)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/mplx/ci?style=flat-square)](https://github.com/nschloe/mplx/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/mplx.svg?style=flat-square)](https://codecov.io/gh/nschloe/mplx)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/mplx.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/mplx)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Install with

```sh
pip install mplx
```

and use in Python with

```python
import mplx
```

See below for what mplx can do.

### Clean line plots

<a href="tests/dufte_comparison.py">
<table width="100%">
  <tr>
  <td width="50%"><img src="https://nschloe.github.io/mplx/ex1-mpl.svg"/></td>
  <td width="50%"><img src="https://nschloe.github.io/mplx/ex1-dufte.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>
    <code>mplx.styles.dufte</code>,
    <code>mplx.ylabel_top</code>,
    <code>mplx.line_labels</code>
    </td>
  </tr>
</table>
</a>

The right plot is created with

```python
import matplotlib.pyplot as plt
import mplx
import numpy as np

# create data
rng = np.random.default_rng(0)
offsets = [1.0, 1.50, 1.60]
labels = ["no balancing", "CRV-27", "CRV-27*"]
x0 = np.linspace(0.0, 3.0, 100)
y = [offset * x0 / (x0 + 1) + 0.1 * rng.random(len(x0)) for offset in offsets]

# plot
with plt.style.context(mplx.styles.dufte):
    for yy, label in zip(y, labels):
        plt.plot(x0, yy, label=label)
    plt.xlabel("distance [m]")
    mplx.ylabel_top("voltage [V]")  # move ylabel to the top, rotate
    mplx.line_labels()  # line labels to the right
    plt.show()
```

The three mplx ingredients are:

- `mplx.styles.dufte`: A minimalistic style
- `mplx.ylabel_top`: Rotate and move the the y-label
- `mplx.line_labels`: Show line labels to the right, with the line color

Further reading and other styles:

- [Remove to improve: data-ink ratio](https://www.darkhorseanalytics.com/blog/data-looks-better-naked)

  <img src="https://nschloe.github.io/mplx/data-ink.webp" width="50%"/>

- [Cereblog, _Remove to improve: Line Graph Edition_](https://youtu.be/bDbJBWvonVI)
- [Show the Data - Maximize the Data Ink Ratio](https://youtu.be/pCp0a5_YIWE)
- [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
- [prettyplotlib](https://github.com/olgabot/prettyplotlib)
- [Wikipedia: Chartjunk](https://en.wikipedia.org/wiki/Chartjunk)

### Clean bar plots

<a href="tests/dufte_comparison.py">
<table width="100%">
  <tr>
  <td width="33%"><img src="https://nschloe.github.io/mplx/bars-mpl.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/mplx/bars-dufte1.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/mplx/bars-dufte2.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>dufte</td>
    <td>dufte with <code>mplx.show_bar_values()</code></td>
  </tr>
</table>
</a>

The right plot is created with

```python
import matplotlib.pyplot as plt
import mplx

labels = ["Australia", "Brazil", "China", "Germany", "Mexico", "United\nStates"]
vals = [21.65, 24.5, 6.95, 8.40, 21.00, 8.55]
xpos = range(len(vals))

with plt.style.context(mplx.styles.dufte_bar):
    plt.bar(xpos, vals)
    plt.xticks(xpos, labels)
    mplx.show_bar_values("{:.2f}")
    plt.title("average temperature [°C]")
    plt.show()
```

The two mplx ingredients are:

- `mplx.styles.dufte_bar`: A minimalistic style for bar plots
- `mplx.show_bar_values`: Show bar values directly at the bars

### Extra styles

mplx contains numerous extra color schemes, e.g.,
[Dracula](https://draculatheme.com/), [Nord](https://www.nordtheme.com/),
[gruvbox](https://github.com/morhetz/gruvbox), and
[Solarized](https://ethanschoonover.com/solarized/),
[the revised Tableau colors](https://www.tableau.com/about/blog/2016/7/colors-upgrade-tableau-10-56782).

<!--pytest-codeblocks:skip-->

```python
import matplotlib.pyplot as plt
import mplx

# use everywhere:
plt.style.use(mplx.styles.dracula)

# use with context:
with plt.style.context(mplx.styles.dracula):
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
|      <img src="https://nschloe.github.io/mplx/github-dark.svg" width="100%">      |
|     <img src="https://nschloe.github.io/mplx/github-dimmed.svg" width="100%">     |
|     <img src="https://nschloe.github.io/mplx/github-light.svg" width="100%">      |
|     <img src="https://nschloe.github.io/mplx/gruvbox-dark.svg" width="100%">      |
|     <img src="https://nschloe.github.io/mplx/gruvbox-light.svg" width="100%">     |
|         <img src="https://nschloe.github.io/mplx/nord.svg" width="100%">          |
|       <img src="https://nschloe.github.io/mplx/one-dark.svg" width="100%">        |
|        <img src="https://nschloe.github.io/mplx/pacoty.svg" width="100%">         |
| <img src="https://nschloe.github.io/mplx/pitaya-smoothie-dark.svg" width="100%">  |
| <img src="https://nschloe.github.io/mplx/pitaya-smoothie-light.svg" width="100%"> |
|    <img src="https://nschloe.github.io/mplx/solarized-dark.svg" width="100%">     |
|    <img src="https://nschloe.github.io/mplx/solarized-light.svg" width="100%">    |
|      <img src="https://nschloe.github.io/mplx/tableau-10.svg" width="100%">       |
|    <img src="https://nschloe.github.io/mplx/tokyo-night-day.svg" width="100%">    |
|   <img src="https://nschloe.github.io/mplx/tokyo-night-night.svg" width="100%">   |
|   <img src="https://nschloe.github.io/mplx/tokyo-night-storm.svg" width="100%">   |

Other styles:

- [John Garrett, _Science Plots_](https://github.com/garrettj403/SciencePlots)
- [Dominik Haitz, _Cyberpunk style_](https://github.com/dhaitz/mplcyberpunk)
- [Dominik Haitz, _Matplotlib stylesheets_](https://github.com/dhaitz/matplotlib-stylesheets)
- [Carlos da Costa, _The Grand Budapest Hotel_](https://github.com/cako/mpl_grandbudapest)
- [Danny Antaki, _vaporwave aesthetics_](https://github.com/dantaki/vapeplot)
- [QuantumBlack Labs, _QuantumBlack_](https://github.com/quantumblacklabs/qbstyles)

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
