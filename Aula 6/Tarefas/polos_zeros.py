import numpy as np
from zplane import zplane

"""
        Z^2 + 1.5Z + 2
D(Z) =  --------------
             Z^2
"""

num = np.array([1, 1.5, 2])
den = np.array([1, 0, 0])

zplane(num, den)
