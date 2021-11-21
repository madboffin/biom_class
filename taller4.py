import numpy as np
import matplotlib.pyplot as plt
from gait_functions import *

filename='JuanDR_Calib01.csv'
data = np.genfromtxt(filename, delimiter='\t',skip_header=3)
fs = 100

# to get initial contact and toe off
sacr = data[:,5:8]
rhee = data[:,11:14]
rtoe = data[:,14:17]
lhee = data[:,23:26]
ltoe = data[:,26:29]

# to get leg length
rmed = data[:,20:23]
lmed = data[:,32:]
lasi = data[:,8:11]
rasi = data[:,2:5]

# three-dimensional plot of data
plt.figure()
ax = plt.axes(projection='3d')
xdata = np.concatenate([sacr[:,0], rasi[:,0], lasi[:,0], rmed[:,0], lmed[:,0]])
ydata = np.concatenate([sacr[:,1], rasi[:,1], lasi[:,1], rmed[:,1], lmed[:,1]])
zdata = np.concatenate([sacr[:,2], rasi[:,2], lasi[:,2], rmed[:,2], lmed[:,2]])
ax.scatter3D(xdata, ydata, zdata, )
plt.show()

# detecting the HJC using Hara's algorithm

# leg length
LLL = get_leglen(lmed, lasi)
LLR = get_leglen(rmed, rasi)
print(f'Largo de piernas. Izquierda: {LLL:.2f} mm, derecha {LLR:.2f} mm')

# hip joint centre
HJCleft = get_hjc(LLL) 
print(f'Coordenadas SACR: {sacr[4,:]}')
print(f'Coordenadas HJC izquierdo: {HJCleft}')
