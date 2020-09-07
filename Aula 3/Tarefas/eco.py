# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import matplotlib.pyplot as plt


# Lendo arquivo como binario
try:
    with open ("alo.pcm", "rb") as file:
        fid = file.read()
        file.close()
except:
    print("Falha ao abrir arquivo")
    exit(0)

entrada = np.frombuffer(fid, dtype = "int16")
tama_loop = len(entrada)

Fs = 8000
t1 = 1.0*10**(-3)
t2 = 1.5*10**(-3)

n = [int(t1*Fs), int(t2*Fs), 0]

# Definição dos ganhos 
a = [0.5, 0.3, 0.2] 
quantidade_ganho = len(a)

tama_delay = int(t2*Fs)
vetor_delay = np.zeros(tama_loop, dtype = "int16");


# Definindo a entrada
vet_saida = np.copy(entrada)


for i in range(quantidade_ganho):
    for j in range(tama_loop):
        vetor_delay[j] = a[i]*entrada[j]
        
        vet_saida = np.concatenate([vet_saida, np.zeros(n[i], dtype = "int16")])
    vet_saida = np.concatenate((vet_saida, vetor_delay))



plt.figure("Figura 1",figsize=(15,8))

# Plotando a saída
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
plt.plot(vet_saida,color='red')


plt.tight_layout()

# Salvando o arquivo de saída
with open("alo_eco.pcm", "wb") as new_file:
    for data in vet_saida:
        new_file.write(data)
    new_file.close()

# Salvando os gráficos
plt.savefig("graficos_eco.png", format="png")


plt.show()
