#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:58:21 2018

@author: bruce
"""

import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import pandas as pd
import craftplot
from craftplot import mplwrap,aps_params,linestyles,set_locator
from your_own_template import your_own_params
import sys

# rcparams's document: https://matplotlib.org/stable/api/matplotlib_configuration_api.html
# font style: https://matplotlib.org/2.0.2/examples/pylab_examples/fonts_demo.html
_parmas=your_own_params()

@mplwrap(_parmas)
def plot_example():

    data=pd.read_csv("test_data.csv",header=None,sep="\s+",skiprows=1)

    #create the plot object
    fig, ax = plt.subplots(nrows=1)

    
    linestyle_MD=linestyles(colors=craftplot.tableau_10,hollow_styles=[True],lines=["--"],markeredge=1.0)

    #plot data
    for i in range(10):
        ax.plot(data[0],data[1]*(i*10+1),**next(linestyle_MD),markersize=3,linewidth=1,label=str(i))

    #set the plot parameters
    ax.legend(loc="best",ncol=2)
    
    #ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"time [ps]")
    ax.set_ylabel(r"$\mathbf{g_{1}(t)}$")
    
    ax.yaxis=set_locator(ax.yaxis,numticks=5)

    fig.tight_layout(pad=0.1) 
    fig.savefig("test_color_Default.png")

plot_example()
