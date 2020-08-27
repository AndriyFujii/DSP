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
    

plt.figure("Gráficos",figsize=(15,12))

# Plotando os gráficos
x = np.linspace(-1, 8, 10)

# Impulso unitário
#pulso = signal.unit_impulse(10, idx = 1)
pulso = unit(x)

plt.subplot(611)
plt.title("Impulso unitário")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, pulso)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Degrau unitário

degrau = step(x)

plt.subplot(612)
plt.title("Degrau unitário")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, degrau)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Seno
x2 = np.linspace(-1, 30, 32)
fo = 100
Fs = 8000
seno = np.sin(2*np.pi*x2*fo/Fs)

plt.subplot(613)
plt.title("Sequência sinusoidal Fo = 100Hz e Fs = 8kHz")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x2, seno)
plt.xticks(np.arange(-1, 30.1, 1))
plt.yticks(np.arange(0, 1.1, 1))

# Exponencial1
exponencial =  0.5 ** x2

plt.subplot(614)
plt.title("Sequência exponencial A=1 e a=0,5")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x2, exponencial)
plt.xticks(np.arange(-1, 30.1, 1))
plt.yticks(np.arange(0, 2.1, 1))

# Exponencial2
exponencial2 =  -0.5 ** x2

plt.subplot(615)
plt.title("Sequência exponencial A=1 e a=-0,5")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x2, exponencial2)
plt.xticks(np.arange(-1, 30.1, 1))
plt.yticks(np.arange(-2, 0.1, 1))

# Exponencial3
exponencial2 =  2 ** x

plt.subplot(616)
plt.title("Sequência exponencial A=1 e a=2")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(1)
plt.stem(x, exponencial2)
plt.xticks(np.arange(-1, 8.1, 1))
plt.yticks(np.arange(0, 256.1, 32))



plt.tight_layout()





# Salvando os gráficos
plt.savefig("graficos_sinais.png", format="png")

plt.show()

