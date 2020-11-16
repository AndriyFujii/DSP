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
FcPB = 600
FcPA = 3000
FcPF_PB = 3000
FcPF_PA = 600
Bw = 200

Bw = Bw / Fs
FcPB = FcPB / Fs
FcPA = FcPA / Fs
FcPF_PB = FcPF_PB / Fs
FcPF_PA = FcPF_PA / Fs
M = 4 / Bw
M = int(M)

h_pb = np.zeros(M)
h_pa = np.zeros(M)
h_pf = np.zeros(M)
h_pf_pb = np.zeros(M)
h_pf_pa = np.zeros(M)

# PB
# Calcula o filtro kernel pb
h_pb = kernelFilter(M, h_pb, FcPB)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pb[i]

for i in range(M):
    h_pb[i] = h_pb[i] / soma

#PA
# Calcula o filtro kernel pb
h_pa = kernelFilter(M, h_pa, FcPA)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pa[i]

for i in range(M):
    h_pa[i] = h_pa[i] / soma

# Transforma de pb para pa
h_pa = -h_pa
h_pa[int(M/2)] += 1


#PF
#PF PB
# Calcula o filtro kernel pb
h_pf_pb = kernelFilter(M, h_pf_pb, FcPF_PB)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pf_pb[i]

for i in range(M):
    h_pf_pb[i] = h_pf_pb[i] / soma

#PF PA
# Calcula o filtro kernel pb
h_pf_pa = kernelFilter(M, h_pf_pa, FcPF_PA)

# Normaliza
soma = 0
for i in range(M):
    soma = soma + h_pf_pa[i]

for i in range(M):
    h_pf_pa[i] = h_pf_pa[i] / soma

# Transforma de pb para pa
h_pf_pa = -h_pf_pa
h_pf_pa[int(M/2)] += 1

h_pf = np.convolve(h_pf_pb, h_pf_pa)

h = np.convolve(h_pa, h_pb)
h = np.convolve(h, h_pf)
with open('coeficientes_eq.dat', 'w') as f:
    for d in h:
        f.write(str(d.astype(np.float16))+",\n")

gb = 0.7
gf = 0.5
ga = 0.2

read_path = "Sweep_3800.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # PB * PA = PF
    data_o_pb = gb * np.convolve(h_pb, data_i, 'same')
    data_o_pf = gf * np.convolve(h_pf, data_i, 'same')
    data_o_pa = ga * np.convolve(h_pa, data_i, 'same')

    
    data_o = data_o_pb + data_o_pf + data_o_pa
    data_o = data_o.astype(dtype='int16')


t = np.arange(0, data_len/Fs, 1 / Fs)


plt.figure("Gráficos",figsize=(15,12))

plt.subplot(511)
plt.title("Entrada")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_i[: len(t)])
#plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))

plt.subplot(512)
plt.title("Saída")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_o[: len(t)])

[w_pb, h_pb] = freqz(h_pb, worN=Fs, fs=1)
[w_pa, h_pa] = freqz(h_pa, worN=Fs, fs=1)
[w_pf, h_pf] = freqz(h_pf, worN=Fs, fs=1)

plt.subplot(513)
plt.title("Resposta em frequência")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w_pb, abs(h_pb))
#plt.plot(w_pb, 20*np.log10(abs(h_pb)))

plt.subplot(514)
plt.title("Resposta em frequência")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w_pa, abs(h_pa))
#plt.plot(w_pa, 20*np.log10(abs(h_pa)))

plt.subplot(515)
plt.title("Resposta em frequência")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w_pf, abs(h_pf))
#plt.plot(w_pf, 20*np.log10(abs(h_pf)))


plt.tight_layout()


file_name = "Sweep10_3800_Equalizador.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)