# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from passa_baixa import *
from passa_alta import *

if __name__ == '__main__':
    sample_rate = 8000
    media_buf = np.zeros(2)
    saida = 0
    
    FcA = 6000
    FcB = 1000
    Fs = sample_rate
    
    # calcula FC
    wcA = 2*np.pi*FcA
    wcB = 2*np.pi*FcB
    
    # F'
    F1 = 2 * Fs
    
    # coeficientes
    aA = wcA/(F1+wcA)
    bA = (wcA-F1)/(F1+wcA)
    aB = wcB/(F1+wcB)
    bB = (wcB-F1)/(F1+wcB)
    
    read_path = "Sweep10_3600.pcm"
    with open(read_path, 'rb') as f:
        buf = f.read()
        data_i = np.frombuffer(buf, dtype='int16')
        data_len = len(data_i)
    
        data_o = PB(data_i, data_len, saida, media_buf, aA, bB) + PA(data_i, data_len, saida, media_buf, aB, bB)
    
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
    
    file_name = "Sweep10_3600_RF.pcm"
    with open(file_name, 'wb') as f:
        for d in data_o:
            f.write(d)