# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


plt.figure("Gráficos",figsize=(15,8))

# Plotando os gráficos
x = np.arange(0, 8, 0,1)
# Impulso unitário
pulso = signal.unit_impulse(8)

plt.subplot(411)
plt.title("Sinal de entrada")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude da saída")
plt.grid(1)
plt.stem(t, pulso)

plt.subplot(412)
plt.title("Sinal de saída")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude da saída")
plt.grid(1)
plt.plot(t, final_data,color='red')

plt.subplot(412)
plt.title("Sinal de saída")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude da saída")
plt.grid(1)
plt.plot(t, final_data,color='red')



plt.tight_layout()

plt.show()



# Salvando os gráficos
plt.savefig("graficos_sinais.png", format="png")

