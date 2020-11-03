# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from passa_baixa import *

def PA(data_i, data_len, saida, media_buf, a, b):
    data_pb = PB(data_i, data_len, saida, media_buf, a, b)
    data_o = data_i - data_pb
    return data_o

if __name__ == '__main__':
    sample_rate = 8000
    media_buf = np.zeros(2)
    saida = 0
    
    Fc = 3000
    Fs = sample_rate
    
    # calcula FC
    wc = 2*np.pi*Fc
    
    # F'
    F1 = 2 * Fs
    
    # coeficientes
    a = wc/(F1+wc)
    b = (wc-F1)/(F1+wc)
    
    read_path = "Sweep10_3600.pcm"
    with open(read_path, 'rb') as f:
        buf = f.read()
        data_i = np.frombuffer(buf, dtype='int16')
        data_len = len(data_i)
    
        data_o = PA(data_i, data_len, saida, media_buf, a, b)
        
    # amostra de 100 ms
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
    
    file_name = "Sweep10_3600_PA.pcm"
    with open(file_name, 'wb') as f:
        for d in data_o:
            f.write(d)