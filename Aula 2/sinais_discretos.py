# -*- coding: utf-8 -*-
"""

@author: Andriy
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def step(t):
    z = []
    for x in t:
        if x > 0.0:
            z.append(1)
        else:
            z.append(0)
    return z

def unit(t):
    z = []
    for x in t:
        if x == 0:
            z.append(1)
        else:
            z.append(0)
    return z
    

plt.figure("Gráficos",figsize=(15,8))

# Plotando os gráficos
x = np.linspace(-1, 8, 10)

# Impulso unitário
#pulso = signal.unit_impulse(10, idx = 1)
pulso = unit(x)

plt.subplot(411)
plt.title("Impulso unitário")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, pulso)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Degrau unitário
degrau = step(x)

plt.subplot(412)
plt.title("Degrau unitário")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, degrau)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Seno
seno = np.sin(x)

plt.subplot(413)
plt.title("Sequência sinusoidal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, seno)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Exponencial
exponencial =  0.5 ** x

plt.subplot(414)
plt.title("Sequência exponencial A=1 e a=0,5")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, exponencial)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 2.1, 1))



plt.tight_layout()





# Salvando os gráficos
plt.savefig("graficos_sinais.png", format="png")

plt.show()

