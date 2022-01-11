# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""
import numpy as np
import matplotlib.pyplot as plt

filename = "JuanDR_Walk01.csv"

data = np.genfromtxt(filename, delimiter='\t',skip_header=5)

fs = 100  # confirmar fs=100Hz
sacr=data[:,5:8]
rhee=data[:,11:14]
rtoe=data[:,14:17]
lhee=data[:,23:26]
ltoe=data[:,26:29]


def get_vtrspeed(x, y, fs):
    """
    Returns vector with speeds
    """
    # removes NaN
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]

    # difference between points
    xdiff = np.diff(x)        
    xdiff = np.square(xdiff)          

    # square values
    ydiff = np.diff(y)
    ydiff = np.square(ydiff)
    
    # calculate speed
    speed = np.sqrt( np.add(xdiff, ydiff) ) / (1/fs)

    return speed


def get_walkspeed(x, y, fs):
    assert len(x)==len(y)

    # gets initial al final values that are not NaN
    start = 0
    end = len(x)-1
    while np.isnan(x[start]) or np.isnan(y[start]):
        start +=1

    while np.isnan(x[end]) or np.isnan(y[end]):
        start -=1
    
    # calculate walking relevant parameters
    time  = len(x)*(1/fs)
    xdiff = x[end] - x[start]
    ydiff = y[end] - y[start]
    speed = np.sqrt(np.sum((xdiff-ydiff)**2)) / time
    return speed


def get_ic(speed, thr=500):
    frames_list = []
    cnt = 0

    # from fist item to second to last
    for k in range(0, len(speed)-1):

        # adds to counter if condition is met
        if (speed[k]>=500) and (speed[k+1]<500):
            cnt += 1
            frames_list.append(k)
      
    return np.array(frames_list)


def get_stride_len(ic_frames):
    stride_len = []
    for k,value in enumerate(ic_frames):
        if k==0: continue
        stride_len.append(np.sqrt(np.sum(np.square(np.add(rhee[ic_frames[k]], -rhee[ic_frames[k-1]])))))
    return stride_len

def get_to(speed, wspeed, thr=0.66):
    frames_list = []
    cnt = 0

    # from fist item to second to last
    for k in range(0, len(speed)-1):

        # adds to counter if condition is met
        if (speed[k]<wspeed*thr) and (speed[k+1]>=wspeed*thr):
            cnt += 1
            frames_list.append(k)
      
    return np.array(frames_list)


# getting IC info
print('Getting IC frames (right first)')
thr = 500
r_speed = get_vtrspeed(rhee[:,0], rhee[:,1], 100)  
l_speed = get_vtrspeed(lhee[:,0], lhee[:,1], 100)
ric_frames = get_ic(r_speed, thr=thr)
lic_frames = get_ic(l_speed, thr=thr)
print(f'{ric_frames + 460}')
print(f'{lic_frames + 460}')

print('Getting stride length')
rstride_len = get_stride_len(ric_frames)
lstride_len = get_stride_len(lic_frames)
print(f'{rstride_len}')
print(f'MEAN: {np.mean(rstride_len):.2f}, STD: {np.std(rstride_len):.2f}')
print(f'{lstride_len}')
print(f'MEAN: {np.mean(lstride_len):.2f}, STD: {np.std(lstride_len):.2f}')

print('Getting stride times')
rstride_time = np.diff(ric_frames) * (1/fs)
lstride_time = np.diff(lic_frames) * (1/fs)
print(rstride_time)
print(lstride_time)

print('Getting step lenth')
rstep_len = [np.sqrt(np.sum(np.square(np.add(rhee[frame,:2], -1*lhee[frame,:2])))) for frame in ric_frames]
lstep_len = [np.sqrt(np.sum(np.square(np.add(rhee[frame,:2], -1*lhee[frame,:2])))) for frame in lic_frames]
print(f'{rstep_len} \n{lstep_len}')

print('Getting step times')
ic_all = np.sort(np.append(ric_frames+460, lic_frames+460))
step_time = np.diff(ic_all) * (1/fs)
print(step_time)

# getting TO info
print('\nGetting TO frames (right first)')
walking_speed = get_walkspeed(rhee[:,0], rhee[:,1], 100)
print(f'walking speed: {walking_speed}')

rtoe_speed = get_vtrspeed(rtoe[:,0], rtoe[:,1], 100)
ltoe_speed = get_vtrspeed(ltoe[:,0], ltoe[:,1], 100)
rto_frames = get_to(rtoe_speed, walking_speed, thr=0.66)
lto_frames = get_to(ltoe_speed, walking_speed, thr=0.66)
print(rto_frames + 380, lto_frames + 380)
