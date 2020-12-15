# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np
import scipy.io.wavfile as wav

    
Fs, x = wav.read("ElectricGuitar.wav")
data_len = len(x)

NORM = 32768

x = np.array(x)
x = x / NORM
    
y = np.copy(x)

gain = 1
Q = -0.2
dist = 8
mix = 1

# Normalization
q = x*gain/np.amax(abs(x))

if(Q == 0):
    z = q / (1-np.exp(-dist*q))
    for i in range(data_len):
        if (q[i] == Q):
            z[i] = 1/dist
else:
    z = (q-Q) / (1-np.exp(-dist*(q-Q)))+Q/(1-np.exp(dist*Q))
    for i in range(data_len):
        if(q[i] == Q):
            z[i] = 1/dist+Q/(1-np.exp(dist*Q))

y = mix*z*np.amax(abs(x))/np.amax(abs(z))+(1-mix)*x
y = y*np.amax(abs(x))/np.amax(abs(y))

y = y * NORM
y = y.astype(dtype='int16')
wav.write("ElectricGuitar_OVERDRIVE.wav", Fs, y)

