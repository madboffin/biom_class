# %%
import numpy as np
import matplotlib.pyplot as plt

from gait_functions import *
from btkTools import *

file_walk='JuanDR_Walk01.c3d'
acq = smartReader(file_walk)
fs = acq.GetPointFrequency()

# relevant markers
sacr = acq.GetPoint("SACR").GetValues()
rhee = acq.GetPoint("RHEE").GetValues()
rtoe = acq.GetPoint("RTOE").GetValues()
lhee = acq.GetPoint("LHEE").GetValues()
ltoe = acq.GetPoint("LTOE").GetValues()

# finding the rotation matrix to place gait direction onto X axis
rot_matrix = rotate_pca(sacr)

# applying rotation: ** from here on the markers are transformed **
sacr = sacr @ rot_matrix
rhee = rhee @ rot_matrix
rtoe = rtoe @ rot_matrix
lhee = lhee @ rot_matrix
ltoe = ltoe @ rot_matrix

# %% Runs the gait analysis on the rotated data

# getting IC info with Gaussianni's mehtod
r_speed = get_vtrspeed(rhee[:,0], rhee[:,2], 100)
l_speed = get_vtrspeed(lhee[:,0], lhee[:,2], 100)
ric_frames = get_ic(r_speed)
lic_frames = get_ic(l_speed)

print('Getting stride length')
rstride_len = get_stride_len(rhee, ric_frames)
lstride_len = get_stride_len(lhee, lic_frames)
print(f'Right stride MEAN: {np.mean(rstride_len):.2f}, STD: {np.std(rstride_len):.2f}')
print(f'Left stride MEAN: {np.mean(lstride_len):.2f}, STD: {np.std(lstride_len):.2f}\n')

# print('Getting stride times')
rstride_time = np.diff(ric_frames) * (1/fs)
lstride_time = np.diff(lic_frames) * (1/fs)

print('Getting step lenth')
rstep_len = [np.sqrt(np.sum(np.square(np.add(rhee[frame,:2], -1*lhee[frame,:2])))) for frame in ric_frames]
lstep_len = [np.sqrt(np.sum(np.square(np.add(rhee[frame,:2], -1*lhee[frame,:2])))) for frame in lic_frames]
print(f'Right step lenghts: {rstep_len} \nLeft step lenghts: {lstep_len}\n')

print('Getting step times')
ic_all = np.sort(np.append(ric_frames, lic_frames))
step_time = np.diff(ic_all) * (1/fs)
print(step_time)

# getting TO info using modified Gaussianni's method
print('\nGetting TO frames (right first)')
walking_speed = get_walkspeed(rhee[:,0], rhee[:,1], 100)
print(f'walking speed: {walking_speed:.2f} mm/s')

rtoe_speed = get_vtrspeed(rtoe[:,0], rtoe[:,2], 100)
ltoe_speed = get_vtrspeed(ltoe[:,0], ltoe[:,2], 100)
rto_frames = get_to(rtoe_speed, walking_speed, thr=0.66)
lto_frames = get_to(ltoe_speed, walking_speed, thr=0.66)

# plotting results

# ploting IC
plt.figure()
plt.title("Velocidad sagital de marcador de talón")
plt.plot(r_speed, label="velocidad pie derecho",c='b')
plt.plot(l_speed, label="velocidad pie izquierdo",c='g')
plt.plot(ric_frames, r_speed[ric_frames], "v", c='b', label="IC derecho")
plt.plot(lic_frames, l_speed[ric_frames], "v", c='g', label="IC izquierdo")
plt.ylabel("Velocidad de marcador [mm/s]")
plt.xlabel("Frame [10 ms por frame]")
plt.legend()
plt.show()

# ploting TO
plt.figure()
plt.title("Velocidad sagital de marcador TOE")
plt.plot(rtoe_speed, label="velocidad pie derecho", c='b')
plt.plot(ltoe_speed, label="velocidad pie izquierdo", c='g')
plt.plot(rto_frames, rtoe_speed[rto_frames], "^", c='b', label="TO derecho")
plt.plot(lto_frames, ltoe_speed[lto_frames], "^", c='g', label="TO izquierdo")
plt.ylabel("Velocidad de marcador [mm/s]")
plt.xlabel("Frame [10 ms por frame]")
plt.legend()
plt.show()

# C3D file creation

# adding HJC points to acquisition object
# smartAppendPoint(acq, "Nuevo_eje", nuevo_eje)

# # writing new c3d file
# new_file_name = f"{file_walk[:-4]}_to_del.c3d"
# print(f"Saving .c3d file as {new_file_name}")

# smartWriter(acq, new_file_name)