# -*- coding: utf-8 -*-
"""
aps.py

"""

__all__ = ['default_params', ]
# Constants from APS Authour Guidelines.
"""
Figures should have a width of a 8.6 cm or 3 3/8 in, the width of a single manuscript column. 
Use a width of 1.5 or 2 columns for more detailed figures. Authors are required to submit all figures electronically for production. 
Preferred formats are .ps, .eps, .pdf, .jpg, and .png; refer to the manuscript Submission Guidelines below for more details. 
Number figures in the order in which they are referred to in the text.

Format figures such that their content and details are readable when they are sized for the journal page. 
Make the height of the smallest capital letters and numerals at least 2 mm and make the diameter of each data point at least 1 mm. 
Make a curve's linewidth at least 0.18 mm (0.5 point). Avoid small open symbols, shading, and cross-hatching in figures.
"""

from .colors import default_color_cycler

width_single_column = 3.375
width_double_column = 6.75

GOLDEN_RATIO = 0.618
# Default ratio for a single plot figure
height_width_ratio = GOLDEN_RATIO * 1.2# = height / width

_width = width_single_column
_height = width_single_column * height_width_ratio

def default_params(colors=default_color_cycler,figure_width=_width,figure_height=_height):
    _params = {'font.family': 'sans-serif',
           'font.serif': ['Times', 'Computer Modern Roman'],
           'font.sans-serif': ['Helvetica', 'Computer Modern Sans serif'],
           'font.size': 9,
           'text.usetex': False,
           # To force LaTeX use Helvetica fonts.
           #'text.latex.preamble': latex_preamble,
           'axes.prop_cycle': default_color_cycler,
           'axes.labelsize': 9,
           'axes.linewidth': 1,

           'figure.figsize': (_width, _height),
           # 'figure.subplot.left' : 0.125,
           # 'figure.subplot.right' : 0.95,
           # 'figure.subplot.bottom' : 0.1,
           # 'figure.subplot.top' : 0.95,

           'savefig.dpi': 600,
           'savefig.format': 'eps',
           # 'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize': 8.5,
           'legend.frameon': False,
           'legend.numpoints': 1,
           'legend.handlelength': 2,
           'legend.scatterpoints': 1,
           'legend.labelspacing': 0.5,
           'legend.markerscale': 0.9,
           'legend.handletextpad': 0.5,  # pad between handle and text
           'legend.borderaxespad': 0.5,  # pad between legend and axes
           'legend.borderpad': 0.5,  # pad between legend and legend content
           'legend.columnspacing': 1,  # pad between each legend column

           # 'text.fontsize' : 8,
           'xtick.labelsize': 8,
           'ytick.labelsize': 8,

           'lines.linewidth': 1,
           'lines.markersize': 4,
           # 'lines.markeredgewidth' : 0,
           # 0 will make line-type markers, such as '+', 'x', invisible

           # Revert some properties to mpl v1 which is more suitable for publishing
           'axes.autolimit_mode': 'round_numbers',
           'axes.xmargin': 0,
           'axes.ymargin': 0,
           'xtick.direction': 'in',
           'xtick.top': True,
           'ytick.direction' : 'in',
           'ytick.right': True,
           }
    return _params