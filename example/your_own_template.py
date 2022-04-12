# -*- coding: utf-8 -*-
"""
aps.py

"""
import sys
sys.path.append('/home/zwq2834/mypackage/craftplot')
from craftplot import default_color_cycler

__all__ = ['your_own_params', ]

width_single_column = 3.375
width_double_column = 6.75

# Default ratio for a single plot figure
height_width_ratio = 1.0/1.618# = height / width

_width = width_single_column
_height = width_single_column * height_width_ratio

def your_own_params(colors=default_color_cycler,figure_width=_width,figure_height=_height):
    _params = {'font.family': 'sans-serif',
           'font.serif': ['Times', 'Computer Modern Roman'],
           'font.sans-serif': ['Helvetica', 'Computer Modern Sans serif'],
           'font.size': 9,
           'font.weight':'semibold',
           'pgf.rcfonts': False,
           'text.usetex': False,
           # To force LaTeX use Helvetica fonts.
           #'text.latex.preamble': [r'\usepackage{siunitx}',
           #                        r'\sisetup{detect-all}',
           #                        r'\usepackage{helvet}',
           #                        r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
           #                        r'\sansmath'],

           'axes.prop_cycle': colors,
           'axes.labelsize': 9,
           'axes.linewidth': 1,
           'axes.unicode_minus': True,
           'axes.labelweight':'semibold',

           'figure.figsize': (figure_width, figure_height),
           # 'figure.subplot.left' : 0.125,
           # 'figure.subplot.right' : 0.95,
           # 'figure.subplot.bottom' : 0.1,
           # 'figure.subplot.top' : 0.95,

           'savefig.dpi': 600,
           'savefig.format': 'png',
           # 'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize': 8.5,
           'legend.frameon': False,
           'legend.numpoints': 1,
           'legend.handlelength': 2,
           'legend.scatterpoints': 1,
           'legend.labelspacing': 0.25,
           'legend.markerscale': 1,
           'legend.handletextpad': 0.5,  # pad between handle and text
           'legend.borderaxespad': 0.5,  # pad between legend and axes
           'legend.borderpad': 0.5,  # pad between legend and legend content
           'legend.columnspacing': 0.75,  # pad between each legend column
           # 'text.fontsize' : 8,

           'xtick.labelsize': 9,
           'ytick.labelsize': 9,

           'xtick.direction': 'in',
           'xtick.major.size': 2.5,
           'xtick.major.width': 0.5,
           'xtick.minor.size': 1.5,
           'xtick.minor.width': 0.5,
           'xtick.minor.visible': True,
           'xtick.minor.bottom': True,

           'xtick.top': True,

           'ytick.direction': 'in',
           'ytick.major.size': 2.5,
           'ytick.major.width': 0.5,
           'ytick.minor.size': 1.5,
           'ytick.minor.width': 0.5,
           'ytick.minor.visible': True,
           'ytick.right': True,

           'lines.linewidth': 0.7,
           'lines.markersize': 3,

           # 'lines.markeredgewidth' : 0,
           # 0 will make line-type markers, such as '+', 'x', invisible
           }
    return _params