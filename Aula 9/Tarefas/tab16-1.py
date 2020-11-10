# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt

def kernelFilter(i, M, h, Fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * np.pi * Fc
        else:
            h[i] = np.sin(2 * np.pi * Fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * (i / M)))


    
x = np.zeros(4999)
y = np.zeros(4999)
h = np.zeros(100)

Fs = 1000
Fc = 0.14
M = 100


for i in range(M):
    if i - M / 2 == 0:
        h[i] = 2 * np.pi * Fc
    else:
        h[i] = np.sin(2 * np.pi * Fc * (i - M / 2)) / (i - M / 2)
    h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * (i / M)))

soma = 0
for i in range(M):
    soma = soma + h[i]

for i in range(M):
    h[i] = h[i] / soma

for j in range(100, len(x)):
    y[i] = 0
    for i in range(M):
        y[j] = y[j] + x[j-i] * h[i]

plt.figure("Gráficos",figsize=(15,15))

plt.title("Saida")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(y)
#plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))
