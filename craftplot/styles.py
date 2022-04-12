# -*- coding: utf-8 -*-
"""
styles.py
=========

Toolkits and constants for plotting styles.

"""

import itertools

# matplotlib styles: https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

from .colors import almost_black, tableau_10

__all__ = ['colors', 'lines',
           'markers', 'markersh', 'marker_types',
           'linestyle_generator', 'linestyles']

_colors = tableau_10
colors = itertools.cycle(_colors)

_lines = ['-', '--', '-.', ':']
lines = itertools.cycle(_lines)

_markers = ['o', 's', 'v', '^', 'D', '<', '>', 'p', 'h']
markers = itertools.cycle(_markers)

# for making hollow markers, use it together with marker_types
_markersh = ['o', 'o', 's', 's', 'v', 'v', '^', '^', 'D', 'D']
markersh = itertools.cycle(_markersh)

_marker_types = [False, True]  # True for hollow markers
marker_types = itertools.cycle(_marker_types)


    
def linestyles(colors=_colors, lines=_lines,
               markers=_markers, hollow_styles=_marker_types,markeredge=1):
    """
    Short name for ``linestyle_generator``.
    To be compatible with previous versions.
    """
    return linestyle_generator(colors, lines, markers, hollow_styles,_mew=markeredge)


def linestyle_generator(colors=_colors, lines=_lines,
                        markers=_markers, hollow_styles=_marker_types,_mew=1):
    """
    Generate a dict for configuring plot line styles.

    The default line style is markers linked by lines, both styles are cycled,
    and hollow markers are included.

    Usage::

      linestyles = linestyle_generator()
      linestyle = linestyles.next()

    Note that all inputs should be iterable objects.
    To exclude one style, just pass empty list or ``None`` to the corresponding argument.
    To include one style but not cycle, just pass a single-element list.
    For example, pass ``lines=['-'] to apply solid line style to all line arts.
    Similarly, passing ``markers=['o']`` will apply filled circle only.

    :param colors: list of colors, (tuple of RGB or #FFFFFF
                or color name string)
    :type colors: list of tuple or list of string or ``None``
    :param lines: list of line styles within ('-', '--', '-.', ':')
    :type lines: list of string,  or ``None``
    :param markers: list of markers (see matplotlib for available markers)
    :type markers: list of charaters,  or ``None``
    :param hollow_styles: True for hollow markers, False for filled markers.
    :param hollow_styles: list of bool,  or ``None``
    :return: dict of parameters of linestyle
    :rtype: dict
    """

    # If both lines and markers are empty or None, do nothing
    is_nothing = False
    if not lines and not markers:
        is_nothing = True

    if colors:
        color_cycle = itertools.cycle(colors)
    else:  # default line color is almost_black
        color_cycle = itertools.cycle([almost_black])

    if lines:
        line_cycle = itertools.cycle(lines)
    else:  # empty list or None supplied, disable line connection
        line_cycle = itertools.cycle([''])

    if markers and hollow_styles:  # solid and hollow markers
        full_markers = itertools.product(markers, hollow_styles)
    elif markers and not hollow_styles:  # all solid markers
        full_markers = itertools.product(markers, [None])
    else:  # no markers
        full_markers = itertools.product(['None'], [None])
    marker_cycle = itertools.cycle(full_markers)

    while True:
        if not is_nothing:
            color = next(color_cycle)
            linestyle = next(line_cycle)
            marker, hollow = next(marker_cycle)
            '''
            if "error_bar" in marker:   
                if hollow is None:  # only filled markers
                    mec = color
                    mfc = color
                elif hollow:  # make hollow markers
                    mec = color
                    mfc = 'None'
                else:  # otherwise, make filled markers
                    mec = color
                    mfc = color
                #print({'color': color, 'linestyle': linestyle,
                    #'marker': marker, 'mec': mec, 'mfc': mfc})
                yield {'color': color, 'linestyle': linestyle,
                    'marker': 'o', 'mec': mec, 'mfc': mfc}
            
            else:
                '''
            if hollow is None:  # only filled markers
                mew = _mew
                mec = color
                mfc = color
            elif hollow:  # make hollow markers
                mew = _mew
                mec = color
                mfc = 'None'
            else:  # otherwise, make filled markers
                mew = _mew
                mec = color
                mfc = color
            yield {'color': color, 'linestyle': linestyle,
                    'marker': marker, 'mew': mew, 'mec': mec, 'mfc': mfc}
        else:
            yield {}

