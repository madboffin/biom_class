import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.index_tricks import AxisConcatenator

filename = "CoR_coordinates.csv"

# code
csv_values = np.genfromtxt(filename, delimiter=',')
csv_r = csv_values[:, :3]
csv_l = csv_values[:, 3:]
sum_sqr = np.sum((csv_l - csv_r)**2, axis=1)
dist = np.sqrt(sum_sqr)

# mean distance between the 2 points
mean_dist = np.mean(dist)
print(mean_dist)


# ********* SECOND PART *********
mid_points = (csv_r + csv_l) / 2

# calculating the distance between midpoints
mid_point_change = np.diff(mid_points, axis=0)
print(mid_point_change)
dist = np.sqrt( np.sum(mid_point_change**2, axis=1) )
ts = 10e-3                       # sampling time of 10ms
mean_vel = np.mean(dist / ts)
print(mean_vel)                  # units of distance per second