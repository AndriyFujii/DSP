# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt

def PB(data_i, data_len, saida, media_buf, a, b):
    data_o = np.zeros_like(data_i)
    for i in range(data_len):
        media_buf[0] = data_i[i]

        # Slides aula 7 tustin
        m = a*media_buf[0] + a*media_buf[1] - b*saida
        saida = m
        data_o[i] = m
        media_buf[1:2] = media_buf[0:1]
    return data_o

if __name__ == '__main__':
    sample_rate = 8000
    media_buf = np.zeros(2)
    saida = 0
    
    Fc = 1000
    Fs = sample_rate
    
    wc = 2*np.pi*Fc
    
    F1 = 2 * Fs
    
    a = wc/(F1+wc)
    b = (wc-F1)/(F1+wc)
    
    read_path = "Sweep10_3600.pcm"
    with open(read_path, 'rb') as f:
        buf = f.read()
        data_i = np.frombuffer(buf, dtype='int16')
        data_len = len(data_i)
    
        data_o = PB(data_i, data_len, saida, media_buf, a, b)
    
    
    t = np.arange(0, data_len/sample_rate, 1 / sample_rate)
    
    
    plt.figure("Gráficos",figsize=(15,12))
    
    plt.subplot(211)
    plt.title("Entrada")
    plt.xlabel("Frequência")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(t, data_i)
    plt.xticks(np.arange(0, 5.1, 1))
    plt.yticks(np.arange(-15000, 15000.1, 5000))
    
    
    plt.subplot(212)
    plt.title("Saida")
    plt.xlabel("Frequência")
    plt.ylabel("Amplitude")
    plt.grid(1)
    plt.plot(t, data_o)
    plt.xticks(np.arange(0, 5.1, 1))
    plt.yticks(np.arange(-15000, 15000.1, 5000))
    
    file_name = "Sweep10_3600_PB.pcm"
    with open(file_name, 'wb') as f:
        for d in data_o:
            f.write(d)