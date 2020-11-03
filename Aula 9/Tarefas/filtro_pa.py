# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

sample_rate = 8000
buffer = np.zeros(2)
saida = 0

Fc = 400
Fs = sample_rate

# calcula FC
wc = 2 * np.pi * Fc

# F'
F1 = 2 * Fs

# coeficientes
a = F1/(F1+wc)
b = (wc-F1)/(F1+wc)

print(a)
print(b)

read_path = "Sweep10_3600.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        buffer[0] = data_i[i]
        m = a * buffer[0] - a * buffer[1] - b * saida
        saida = m
        
        data_o[i] = m
        
        # deslocamento
        buffer[1:2] = buffer[0:1]

# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)



plt.figure("Gráficos",figsize=(15,15))
    
plt.subplot(311)
plt.title("Entrada")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_i)
plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))


plt.subplot(312)
plt.title("Saida")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_o)
plt.xticks(np.arange(0, 5.1, 1))
#plt.yticks(np.arange(-15000, 15000.1, 5000))

# funcao de transferencia
num = [F1, -F1]
den = [F1+wc, wc-F1]
[w, h] = freqz(num, den, worN=Fs, fs=Fs)

plt.subplot(313)
plt.title("Mangnitude da resposta")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xticks(np.arange(0, 4000.1, 500))
#plt.yticks(np.arange(0, -60, 20))


file_name = "Sweep10_3600_Result.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)