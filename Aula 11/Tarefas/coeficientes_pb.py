# -*- coding: utf-8 -*-
"""

@author: Andriy
"""
import numpy as np

def kernelFilter(M, h, Fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * np.pi * Fc
        else:
            h[i] = np.sin(2 * np.pi * Fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * (i / M)))
    return h

Fs = 8000
Fc = 800
Bw = 200

# Normalizando
Bw = Bw / Fs
Fc = Fc / Fs
M = 4 / Bw
M = int(M)

h = np.zeros(M)

# Calcula o filtro kernel pb
h = kernelFilter(M, h, Fc)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h[i]

for i in range(M):
    h[i] = h[i] / soma

file_name = "coeficientes.dat"
with open(file_name, 'w') as f:
    for d in h:
        f.write(str(d.astype(np.float16)) + ",\n")