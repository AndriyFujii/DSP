# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, k) : 
    ret = np.cumsum(data, dtype=float)
    ret[k:] = ret[k:] - ret[:-k] 
    return ret[k - 1:] / k


# Lendo arquivo como binario
try:
    with open ('wn.pcm', 'rb') as file:
        fid = file.read ()
        file.close()
except:
    print("Falha ao abrir arquivo")
    exit(0)
    
entrada = np.frombuffer (fid, dtype = 'int16')
itera = len(entrada) #N

# Tamanho da media
# k = 4, 8 , 16, 32, 64, 128, 256, 512, 1024
k = 512

saida = moving_average(entrada, k)

plt.figure("Figura 1",figsize=(15,8))

plt.subplot(211)
plt.title("Sinal de entrada")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude da saída")
plt.grid(1)
plt.plot(entrada)

plt.subplot(212)
plt.title("Sinal de saída")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude da saída")
plt.grid(1)
plt.plot(saida,color='red')

plt.tight_layout()
plt.savefig("graficos_media_movel.png", format="png")

# Salvando o arquivo de saída
with open("wn_media_movel.pcm", "wb") as new_file:
    for x in saida:
        new_file.write(x)
new_file.close()

plt.show()