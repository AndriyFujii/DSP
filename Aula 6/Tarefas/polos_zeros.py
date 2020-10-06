# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict


def zplane(z, p):
    """Plot the complex z-plane given zeros and poles.
    """

    # get a figure/plot
    ax = plt.subplot(2, 2, 1)

    # Add unit circle and zero axes
    unit_circle = patches.Circle((0, 0), radius=1, fill=False,
                                 color='black', ls='solid', alpha=0.1)
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    axhline(0, color='0.7')

    # Plot the poles and set marker properties
    poles = plt.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5)

    # Plot the zeros and set marker properties
    zeros = plt.plot(z.real, z.imag, 'o', markersize=9,
                     color='none', alpha=0.5,
                     markeredgecolor=poles[0].get_color(),  # same color as poles
                     )

    # Scale axes to fit
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])

    plt.show()


# N = [1, 1.5, 2]
# D = [1, 0, 0]
# N = [1, 0.6]
# D = [1, 0.6, 0.2]
N = [1, 0.8]
D = [1, 1, 0.41]

zeros = np.roots(N)
poles = np.roots(D)

print(zeros)
print(poles)

zplane(zeros, poles)