# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np

filename = "JuanDR_Walk01.csv"

# TODO: add your code here
data = np.genfromtxt(filename,delimiter='\t',skip_header=5)
rh=data[:,14:17]
sacr=data[:,5:8]

velocidadsacr=np.diff(sacr)
