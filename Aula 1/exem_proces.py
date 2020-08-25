# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as matp


# Lendo arquivo como binario
try:
    with open ("alo.pcm", "rb") as file:
        fid = file.read()
        file.close()
except:
    print("Falha ao abrir arquivo")
    exit(0)

s = np.frombuffer(fid, dtype = "int16")
len_data = len(s)
itera = len(s)

ganho = .5

# Executa o processamento
final_data = np.ones_like(s)
for i in range(itera):
    final_data[i] = s[i] * ganho


matp.figure("Figura 1",figsize=(15,8))

# Plotando a saída
matp.subplot(211)
matp.title("Sinal de entrada")
matp.xlabel("Número de amostras")
matp.ylabel("Amplitude da saída")
matp.grid(1)
matp.plot(s)

matp.subplot(212)
matp.title("Sinal de saída")
matp.xlabel("Número de amostras")
matp.ylabel("Amplitude da saída")
matp.grid(1)
matp.plot(final_data,color='red')


matp.tight_layout()

matp.show()

# Salvando o arquivo de saída
with open("sinal_saida.pcm", "wb") as new_file:
    for data in final_data:
        new_file.write(data)
    new_file.close()

# Salvando os gráficos
matp.savefig("graficos_sinais.png", format="png")

