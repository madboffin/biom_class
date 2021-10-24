# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import matplotlib.pyplot as plt

filename = "JuanDR_Walk01.csv"

# TODO: add your code here

data = np.genfromtxt(filename, delimiter='\t',skip_header=5)
rh=data[:,14:17]
sacr=data[:,5:8]

fs = 100

sacr=data[:,5:8]
rtoe=data[:,14:17]
rhee=data[:,11:14]


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
    """
    Gets walking speed from initial and final points
    """
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


def get_ic(speed, thr):
  frames_list = []
  cnt = 0

  # from fist item to second to last
  for k in range(0, len(speed)-1):

    # adds to counter if condition is met
    if (speed[k]>=500) and (speed[k+1]<500):
        cnt += 1
        frames_list.append(k)
      
  return np.array(frames_list)


v_speed = get_vtrspeed(rhee[:,0], rhee[:,1], 100)
thr = 500
print(get_ic(v_speed, thr=thr) + 480)
