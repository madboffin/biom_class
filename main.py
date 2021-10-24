# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import matplotlib.pyplot as plt

filename = "JuanDR_Walk01.csv"

# TODO: add your code here
data = np.genfromtxt(filename,delimiter='\t',skip_header=5)
rh=data[:,11:14]
rt=data[:,17:20]
sacr=data[:,5:8]
#zsacr=sacr[:,2]
velocidadrh=np.absolute(np.diff(rh[:,2]))
#print(zsacr)
plt.plot(velocidadrh)
plt.show()
