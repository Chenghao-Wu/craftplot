# -*- coding: utf-8 -*-
"""
colors.py
=========

A set of colors and color maps as provided by python package `palettable` (https://jiffyclub.github.io/palettable).

"""

import numpy as np
import matplotlib
from palettable.colorbrewer.qualitative import Set1_9
from palettable.tableau import Tableau_10, Tableau_20
from palettable import cubehelix

#from palettable.scientific.sequential import Devon_6,Hawaii_6,LaPaz_6,Oleron_6,Turku_6
from palettable.scientific.diverging import Roma_3,Roma_4,Roma_5,Roma_6,Roma_7,Roma_8,Roma_9,Roma_10,Roma_11,Roma_12,Roma_13,Roma_14
from palettable.scientific.diverging import Vik_3,Vik_4,Vik_5,Vik_6,Vik_7,Vik_8,Vik_9,Vik_10,Vik_11,Vik_12,Vik_13,Vik_14

#from palettable.colorbrewer.diverging import Spectral_3
#from palettable.matplotlib import Plasma_10
from matplotlib import cm

from cycler import cycler

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

# ColorBrewer
# by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. For more information on ColorBrewer, see:
# - Flash-based interactive map:
# http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
# http://bl.ocks.org/mbostock/5577023
# https://jiffyclub.github.io/palettable/colorbrewer
#
# ColorBrewer scale 'Qualitative.Set1'.
# This one has nice "traditional" colors like reds and blues
# It is suitable for multi-line plots and category items.
brewer_set1 = Set1_9.mpl_colors
# Remove the sixth color (yellow) which is too bright
brewer_set1.pop(5)
# Swap the red and blue to let blue come first
brewer_set1[0], brewer_set1[1] = brewer_set1[1], brewer_set1[0]
# Add a decent black color to this list
brewer_set1.append(almost_black)

# Tableau 10 & 20 Classic
# See: https://jiffyclub.github.io/palettable/tableau/
# Another great qualitative set of colors suitable for multi-line plots.
# 10 and 20 are number of colors in the list.
tableau_10 = Tableau_10.mpl_colors
# Add a decent black color
tableau_10.append(almost_black)
# Swap orange and red
tableau_10[1], tableau_10[3] = tableau_10[3], tableau_10[1]
# swap orange and purple
# now table_au has similar sequence to brewer_set1
tableau_10[3], tableau_10[4] = tableau_10[4], tableau_10[3]
# This is 20-color Tableau which contains light version of tableau_10
tableau_20 = Tableau_20.mpl_colors

#default_color_cycler = cycler('color', cubehelix.cubehelix3_16_r.mpl_colors)
default_color_cycler = cycler('color', brewer_set1)


def rainbow(number_colors=10):
    colors_ = cm.get_cmap('rainbow', number_colors)(np.linspace(0, 1, number_colors))
    colors=[]
    for ii in colors_:
        color=(ii[0],ii[1],ii[2])
        colors.append(color)
    return colors

def Vik(number_colors=10):
    colors_={3:Vik_3.mpl_colors,4:Vik_4.mpl_colors,5:Vik_5.mpl_colors,6:Vik_6.mpl_colors,7:Vik_7.mpl_colors,8:Vik_8.mpl_colors,9:Vik_9.mpl_colors,10:Vik_10.mpl_colors}
    colors=colors_[number_colors]
    return colors

def Roma(number_colors=10):
    colors_={3:Roma_3.mpl_colors,4:Roma_4.mpl_colors,5:Roma_5.mpl_colors,6:Roma_6.mpl_colors,7:Roma_7.mpl_colors,8:Roma_8.mpl_colors,9:Roma_9.mpl_colors,10:Roma_10.mpl_colors}
    colors=colors_[number_colors]
    return colors

def set_locator(axis,numticks=100,base=10):
    locmaj = matplotlib.ticker.LogLocator(base=base, subs=(1.0, ), numticks=numticks)
    axis.set_major_locator(locmaj)
    locmin = matplotlib.ticker.LogLocator(base=base, subs=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],numticks=1000)
    axis.set_minor_locator(locmin)
    axis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    return axis