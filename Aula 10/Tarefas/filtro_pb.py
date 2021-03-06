# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def kernelFilter(M, h, Fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * np.pi * Fc
        else:
            h[i] = np.sin(2 * np.pi * Fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * np.cos(2 * np.pi * (i / M)))
    return h

Fs = 8000
Fc = 1000
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


with open('coeficientes_pb.dat', 'w') as f:
    for d in h:
        f.write(str(d.astype(np.float16))+",\n")

read_path = "Seno_600.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    data_o = np.convolve(h, data_i)
    data_o = data_o.astype(dtype='int16')


t = np.arange(0, data_len/Fs, 1 / Fs)


plt.figure("Gráficos",figsize=(15,12))

plt.subplot(411)
plt.title("Entrada")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_i[: len(t)])
#plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))

plt.subplot(412)
plt.title("Saída")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_o[: len(t)])

[w, h] = freqz(h, worN=Fs, fs=1)

plt.subplot(413)
plt.title("Resposta em frequência")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, abs(h))

plt.subplot(414)
plt.title("Resposta em frequência (dB)")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, 20*np.log10(abs(h)))

plt.tight_layout()


file_name = "Sweep10_3800_PB.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)