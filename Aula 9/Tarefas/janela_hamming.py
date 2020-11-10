# -*- coding: utf-8 -*-
"""


@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

sample_rate = 8000
M = 2

i = np.arange(0, M, 1/sample_rate)

# função hamming do livro cap 16 equação 16-1
w_i = 0.54 - 0.46 * np.cos(2*np.pi*i/M)


plt.figure("Gráficos",figsize=(15,15))
    
plt.subplot(211)
plt.title("Amplitude")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(i, w_i)


[w, h] = freqz(w_i, worN=sample_rate, fs=1)

plt.subplot(212)
plt.title("Magnitude")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, 20 * np.log10(abs(h)))

