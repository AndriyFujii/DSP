# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt

def kernelFilter(M, h, Fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * np.pi * Fc
        else:
            h[i] = np.sin(2 * np.pi * Fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * (i / M)))
    return h
        
sample_rate = 8000        

# M precisa ser par
M = 1000
Fc = 0.02

h = np.zeros(M)
h = kernelFilter(M, h, Fc)


plt.figure("Gráficos",figsize=(15,15))
    
plt.title("Filtro kernel")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(h)
#plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))

