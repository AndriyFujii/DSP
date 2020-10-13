# -*- coding: utf-8 -*-
"""

@author: Andriy
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a = 0.5
w = np.arange(-1*np.pi, 1*np.pi, np.pi/100)

num = 1
den = 1 - a * np.exp(-1j*w) # (complex(0, -1)*w) # 1-a^(-j*w) 
x = num/den

mod_x = np.absolute(x)
fase_x = np.angle(den)

plt.figure("Gráficos",figsize=(15,12))

# Plotando os gráficos
x = np.linspace(-1, 8, 10)


plt.subplot(211)
plt.title("Mod x")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.plot(mod_x)
plt.xticks(np.arange(-1, 200.1, 25))
plt.yticks(np.arange(0, 2.1, 0.5))


plt.subplot(212)
plt.title("Fase X")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.plot(fase_x)
plt.xticks(np.arange(-1, 200.1, 25))
plt.yticks(np.arange(-1, 1.1, 0.5))


plt.tight_layout()


# Salvando os gráficos
plt.savefig("graficos_sinais.png", format="png")

plt.show()

