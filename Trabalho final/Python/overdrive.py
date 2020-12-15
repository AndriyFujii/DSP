# -*- coding: utf-8 -*-
"""

@author: Andriy
"""

import numpy as np

    
read_path = "Seno.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

NORM = 32768

data_i = np.array(data_i)
data_i = data_i / NORM
    
data_o = np.copy(data_i)
th = 1/3

for i in range(data_len):
    # abs para comparar
    if(data_i[i] < 0):
        abs_data_i = -1*data_i[i]
    else:
        abs_data_i = data_i[i]
    
    # overdrive
    # 0 <= x < 1/3
    # f(x) = 2x
    if(abs_data_i < th):
        data_o[i] = 2*data_i[i]
    # 2/3 < x <= 1
    # f(x) = 1
    elif(abs_data_i > 2*th):
        if(data_i[i] > 0):
            data_o[i] = 0.99
        else:
            data_o[i] = -0.99
    # 1/3 <= x <= 2/3
    # f(x) = (3-(2-3x)^2)/3
    else:
        if(data_i[i] > 0):
            data_o[i] = (2-3*data_i[i]) * (2-3*data_i[i])
            data_o[i] = 3 - data_o[i]
            data_o[i] = data_o[i] / 3
        else:
            data_o[i] = (2-3*(-1*data_i[i])) * (2-3*(-1*data_i[i]))
            data_o[i] = 3 - data_o[i]
            data_o[i] = -data_o[i] / 3

data_o = data_o * NORM
data_o = data_o.astype(dtype='int16')

file_name = "Seno_OD.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)

