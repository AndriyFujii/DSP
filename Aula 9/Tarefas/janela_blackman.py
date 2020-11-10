# -*- coding: utf-8 -*-
"""


@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz


sample_rate = 8000
M = 2

# para calcular os valores
i = np.arange(0, M, 1/sample_rate)

# função sinc do livro cap 16 equação 16-2
w_i = 0.42 - 0.5 * np.cos(2*np.pi*i/M) - 0.08 * np.cos(4*np.pi*i/M)

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