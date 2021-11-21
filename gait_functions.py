import numpy as np
import matplotlib.pyplot as plt

def fixna_sides(x, y):
    # gets initial and final values that are not NaN

    start = 0
    end = len(x)-1
    
    # try to use this function on vector with more than 1 value per row
    if x.ndim>1:
        while any(np.isnan(x[start])) or any(np.isnan(y[start])): start +=1
        while any(np.isnan(x[end])) or any(np.isnan(y[end])): start -=1
    else:
        while np.isnan(x[start]) or np.isnan(y[start]): start +=1
        while np.isnan(x[end]) or np.isnan(y[end]): start -=1

    x_fixed = x[start:end+1]
    y_fixed = y[start:end+1]

    return start, end, x_fixed, y_fixed


def fixna_sides_1D(x):
    # gets initial and final values that are not NaN for a vector
    start = 0
    end = len(x)-1
    
    while np.isnan(x[start]):
        start +=1

    while np.isnan(x[end]):
        start -=1

    x_fixed = x[start:end+1]

    return start, end, x_fixed


def get_intraf_distance(x, y):
    # difference between frames, excpects 1d vector
    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # square values
    xdiff = np.square(xdiff)    
    ydiff = np.square(ydiff)

    distance = np.sqrt( np.add(xdiff, ydiff) ) 

    return distance


def get_distance(p1, p2):
    # euclidean distance between two points
    return np.sqrt(np.sum((p1-p2)**2))


def get_vdistances(x, y):
    # euclidian distances between points of vectors
    return np.sqrt(np.sum(np.square(x-y), axis=1))


def get_vtrspeed(x, y, fs):
    """
    Returns vector of speeds
    """
    # gets initial and final values that are not NaN
    _s, _e, x, y = fixna_sides(x, y)

    v_distance = get_intraf_distance(x, y)
    v_speed = v_distance / (1/fs)

    return v_speed


def get_walkspeed(x, y, fs):
    """
    gets walking speed 
    """
    assert len(x)==len(y)

    # gets initial and final values that are not NaN
    start, end, _x, _y = fixna_sides(x, y)
    
    # calculate relevant walking parameters
    time  = len(x)*(1/fs)
    xdiff = x[end] - x[start]
    ydiff = y[end] - y[start]
    distance = get_distance(xdiff, ydiff)
    speed    = distance / time

    return speed


def get_ic(speed, thr=500):
    """
    gets initial contact frames using Ghoussayni's method (2007)
    500 mm/s
    """
    frames_list = []
    cnt = 0

    # from fist item to second to last
    for k in range(0, len(speed)-1):

        # adds to counter if condition is met
        if (speed[k]>=thr) and (speed[k+1]<thr):
            cnt += 1
            frames_list.append(k)
      
    return np.array(frames_list)


def get_to(speed, wspeed, thr=0.66):
    """
    gets toe off frames using modified gaussianni
    """
    frames_list = []
    cnt = 0

    # from fist item to second to last
    for k in range(0, len(speed)-1):

        # adds to counter if condition is met
        if (speed[k]<wspeed*thr) and (speed[k+1]>=wspeed*thr):
            cnt += 1
            frames_list.append(k)
      
    return np.array(frames_list)


def get_stride_len(ic_frames):
    """
    gets stride length from conctact frames
    """
    stride_len = []
    for k,value in enumerate(ic_frames):
        if k==0: continue
        stride_len.append(np.sqrt(np.sum(np.square(np.add(rhee[ic_frames[k]], -rhee[ic_frames[k-1]])))))
    return stride_len


def get_leglen(med, asi):
    # takes missing values from beginning and ending of the arrays
    _s, _e, med, asi = fixna_sides(med, asi)

    # finds the distances between the points in two arrays
    distances = get_vdistances(med, asi)

    # returns median value to avoid outliers
    return np.median(distances)


def get_hjc(LL):
    """
    gets the HJC using Hara 2016 method
    Leg Length (LL) must be in mm
    """
    x = 11-0.063*LL
    y =  8+0.086*LL
    z = -9-0.078*LL
    return x, y, z