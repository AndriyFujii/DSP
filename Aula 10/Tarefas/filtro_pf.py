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
Fc1 = 600
Fc2 = 3000
Bw = 200

Bw = Bw / Fs
Fc1 = Fc1 / Fs
Fc2 = Fc2 / Fs
M = 4 / Bw
M = int(M)

h_pb = np.zeros(M)
h_pa = np.zeros(M)

# Calcula o filtro kernel pb
h_pb = kernelFilter(M, h_pb, Fc2)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pb[i]

for i in range(M):
    h_pb[i] = h_pb[i] / soma


# Calcula o filtro kernel pb
h_pa = kernelFilter(M, h_pa, Fc1)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pa[i]

for i in range(M):
    h_pa[i] = h_pa[i] / soma

# Transforma de pb para pa
h_pa = -h_pa
h_pa[int(M/2)] += 1

h = np.convolve(h_pa, h_pb, 'same')

with open('coeficientes_pf.dat', 'w') as f:
    for d in h:
        f.write(str(d.astype(np.float16))+",\n")

read_path = "Sweep_3800.pcm"
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

[w_pb, h_pb] = freqz(h_pb, worN=Fs, fs=1)
[w_pa, h_pa] = freqz(h_pa, worN=Fs, fs=1)
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


file_name = "Sweep10_3800_PF.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)