# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as matp
from scipy import signal


matp.figure("Gráficos",figsize=(15,8))

# Plotando os gráficos
t = np.arange(0, 8, 0,1)
# Impulso unitário
pulso = signal.unit_impulse(8)

matp.subplot(411)
matp.title("Sinal de entrada")
matp.xlabel("Número de amostras")
matp.ylabel("Amplitude da saída")
matp.grid(1)
matp.stem(t, pulso)

matp.subplot(412)
matp.title("Sinal de saída")
matp.xlabel("Número de amostras")
matp.ylabel("Amplitude da saída")
matp.grid(1)
matp.plot(t, final_data,color='red')

matp.subplot(412)
matp.title("Sinal de saída")
matp.xlabel("Número de amostras")
matp.ylabel("Amplitude da saída")
matp.grid(1)
matp.plot(t, final_data,color='red')



matp.tight_layout()

matp.show()

# Salvando o arquivo de saída
with open("sinal_saida.pcm", "wb") as new_file:
    for data in final_data:
        new_file.write(data)
    new_file.close()

# Salvando os gráficos
matp.savefig("graficos_sinais.png", format="png")

