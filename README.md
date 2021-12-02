<p align="center">
  <a href="https://github.com/nschloe/matplotx"><img alt="matplotx" src="https://nschloe.github.io/matplotx/matplotx-logo.svg" width="55%"></a>
  <p align="center">Some useful extensions for <a href="https://matplotlib.org/">Matplotlib</a>.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/matplotx.svg?style=flat-square)](https://pypi.org/project/matplotx/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/matplotx.svg?style=flat-square)](https://pypi.org/project/matplotx/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/matplotx.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/matplotx)
[![Downloads](https://pepy.tech/badge/matplotx/month)](https://pepy.tech/project/matplotx)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/matplotx/ci?style=flat-square)](https://github.com/nschloe/matplotx/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/matplotx.svg?style=flat-square)](https://codecov.io/gh/nschloe/matplotx)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/matplotx.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/matplotx)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Install with

```sh
pip install matplotx
```

and use in Python with

```python
import matplotx
```

See below for what matplotx can do.

### Clean line plots (dufte)

<a href="tests/dufte_comparison.py">
<table width="100%">
  <tr>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/ex1-mpl.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/ex1-dufte.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/ex1-dufte-dracula.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>
    <code>matplotx.styles.dufte</code>,
    <code>matplotx.ylabel_top</code>,
    <code>matplotx.line_labels</code>
    </td>
    <td>
    <code>matplotx.styles.dracula | matplotx.styles.dufte</code>
    </td>
  </tr>
</table>
</a>

The middle plot is created with

```python
import matplotlib.pyplot as plt
import matplotx
import numpy as np

# create data
rng = np.random.default_rng(0)
offsets = [1.0, 1.50, 1.60]
labels = ["no balancing", "CRV-27", "CRV-27*"]
x0 = np.linspace(0.0, 3.0, 100)
y = [offset * x0 / (x0 + 1) + 0.1 * rng.random(len(x0)) for offset in offsets]

# plot
with plt.style.context(matplotx.styles.dufte):
    for yy, label in zip(y, labels):
        plt.plot(x0, yy, label=label)
    plt.xlabel("distance [m]")
    matplotx.ylabel_top("voltage [V]")  # move ylabel to the top, rotate
    matplotx.line_labels()  # line labels to the right
    plt.show()
```

The three matplotx ingredients are:

- `matplotx.styles.dufte`: A minimalistic style
- `matplotx.ylabel_top`: Rotate and move the the y-label
- `matplotx.line_labels`: Show line labels to the right, with the line color

You can also combine dufte with any other style (see below) with

<!--pytest-codeblocks:skip-->

```python
plt.style.use(matplotx.styles.dracula | matplotx.styles.dufte)
```

(This uses the Python 3.10 dict merge operator `|`. If you're using an older Python version, you have to use, e.g., `{**x, **y}`.)

Further reading and other styles:

- [Remove to improve: data-ink ratio](https://www.darkhorseanalytics.com/blog/data-looks-better-naked)

  <img src="https://nschloe.github.io/matplotx/data-ink.webp" width="50%"/>

- [Cereblog, _Remove to improve: Line Graph Edition_](https://youtu.be/bDbJBWvonVI)
- [Show the Data - Maximize the Data Ink Ratio](https://youtu.be/pCp0a5_YIWE)
- [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
- [prettyplotlib](https://github.com/olgabot/prettyplotlib)
- [Wikipedia: Chartjunk](https://en.wikipedia.org/wiki/Chartjunk)

### Clean bar plots

<a href="tests/dufte_comparison.py">
<table width="100%">
  <tr>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/bars-mpl.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/bars-dufte1.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/matplotx/bars-dufte2.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>dufte</td>
    <td>dufte with <code>matplotx.show_bar_values()</code></td>
  </tr>
</table>
</a>

The right plot is created with

```python
import matplotlib.pyplot as plt
import matplotx

labels = ["Australia", "Brazil", "China", "Germany", "Mexico", "United\nStates"]
vals = [21.65, 24.5, 6.95, 8.40, 21.00, 8.55]
xpos = range(len(vals))

with plt.style.context(matplotx.styles.dufte_bar):
    plt.bar(xpos, vals)
    plt.xticks(xpos, labels)
    matplotx.show_bar_values("{:.2f}")
    plt.title("average temperature [°C]")
    plt.show()
```

The two matplotx ingredients are:

- `matplotx.styles.dufte_bar`: A minimalistic style for bar plots
- `matplotx.show_bar_values`: Show bar values directly at the bars

### Extra styles

matplotx contains numerous extra color schemes, e.g.,
[Dracula](https://draculatheme.com/), [Nord](https://www.nordtheme.com/),
[gruvbox](https://github.com/morhetz/gruvbox), and
[Solarized](https://ethanschoonover.com/solarized/),
[the revised Tableau colors](https://www.tableau.com/about/blog/2016/7/colors-upgrade-tableau-10-56782).

<!--pytest-codeblocks:skip-->

```python
import matplotlib.pyplot as plt
import matplotx

# use everywhere:
plt.style.use(matplotx.styles.dracula)

# use with context:
with plt.style.context(matplotx.styles.dracula):
    pass
```

|    <img src="https://nschloe.github.io/matplotx/aura-dark-soft.svg" width="100%">     |
| :-----------------------------------------------------------------------------------: |
|       <img src="https://nschloe.github.io/matplotx/aura-dark.svg" width="100%">       |
|       <img src="https://nschloe.github.io/matplotx/ayu-dark.svg" width="100%">        |
|       <img src="https://nschloe.github.io/matplotx/ayu-light.svg" width="100%">       |
|      <img src="https://nschloe.github.io/matplotx/ayu-mirage.svg" width="100%">       |
|    <img src="https://nschloe.github.io/matplotx/challenger-deep.svg" width="100%">    |
|        <img src="https://nschloe.github.io/matplotx/dracula.svg" width="100%">        |
|      <img src="https://nschloe.github.io/matplotx/github-dark.svg" width="100%">      |
|     <img src="https://nschloe.github.io/matplotx/github-dimmed.svg" width="100%">     |
|     <img src="https://nschloe.github.io/matplotx/github-light.svg" width="100%">      |
|     <img src="https://nschloe.github.io/matplotx/gruvbox-dark.svg" width="100%">      |
|     <img src="https://nschloe.github.io/matplotx/gruvbox-light.svg" width="100%">     |
|         <img src="https://nschloe.github.io/matplotx/nord.svg" width="100%">          |
|       <img src="https://nschloe.github.io/matplotx/one-dark.svg" width="100%">        |
|        <img src="https://nschloe.github.io/matplotx/pacoty.svg" width="100%">         |
| <img src="https://nschloe.github.io/matplotx/pitaya-smoothie-dark.svg" width="100%">  |
| <img src="https://nschloe.github.io/matplotx/pitaya-smoothie-light.svg" width="100%"> |
|    <img src="https://nschloe.github.io/matplotx/solarized-dark.svg" width="100%">     |
|    <img src="https://nschloe.github.io/matplotx/solarized-light.svg" width="100%">    |
|      <img src="https://nschloe.github.io/matplotx/tableau-10.svg" width="100%">       |
|      <img src="https://nschloe.github.io/matplotx/tableau-20.svg" width="100%">       |
|    <img src="https://nschloe.github.io/matplotx/tokyo-night-day.svg" width="100%">    |
|   <img src="https://nschloe.github.io/matplotx/tokyo-night-night.svg" width="100%">   |
|   <img src="https://nschloe.github.io/matplotx/tokyo-night-storm.svg" width="100%">   |

Other styles:

- [John Garrett, _Science Plots_](https://github.com/garrettj403/SciencePlots)
- [Dominik Haitz, _Cyberpunk style_](https://github.com/dhaitz/mplcyberpunk)
- [Dominik Haitz, _Matplotlib stylesheets_](https://github.com/dhaitz/matplotlib-stylesheets)
- [Carlos da Costa, _The Grand Budapest Hotel_](https://github.com/cako/mpl_grandbudapest)
- [Danny Antaki, _vaporwave aesthetics_](https://github.com/dantaki/vapeplot)
- [QuantumBlack Labs, _QuantumBlack_](https://github.com/quantumblacklabs/qbstyles)

### Contour plots for functions with discontinuities

| <img src="https://nschloe.github.io/matplotx/contour-mpl.svg" width="100%"> | <img src="https://nschloe.github.io/matplotx/contour-matplotx.svg" width="100%"> |
| :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
|                                `plt.contour`                                |                         `matplotx.contour(max_jump=1.0)`                         |

Matplotlib has problems with contour plots of functions that have discontinuities. The
software has no way to tell discontinuities and very sharp, but continuous cliffs apart,
and contour lines will be drawn along the discontinuity.

matplotx improves upon this by adding the parameter `max_jump`. If the difference between
two function values in the grid is larger than `max_jump`, a discontinuity is assumed
and no line is drawn. Similarly, `min_jump` can be used to highlight the discontinuity.

As an example, take the function `imag(log(Z))` for complex values Z. Matplotlib's
contour lines along the negative real axis are wrong.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotx

x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

vals = np.imag(np.log(Z))

# plt.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0])  # draws wrong lines

matplotx.contour(X, Y, vals, levels=[-2.0, -1.0, 0.0, 1.0, 2.0], max_jump=1.0)
matplotx.discontour(X, Y, vals, min_jump=1.0, linestyle=":", color="r")

plt.gca().set_aspect("equal")
plt.show()
```

Relevant discussions:

- [matplotlib/issues/21348](https://github.com/matplotlib/matplotlib/issues/21348)

### License

This software is published under the [MIT license](LICENSE).
