"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
from __future__ import print_function
from pprint import pprint
import datetime
import random
import numpy as np

# seeding the random number generator
random . seed(datetime . datetime . now() . year)


def point_cloud_generator(n=10):
    """
    Helper function to make an array having shape (n, 3)
    """
    _array = []
    for rows in range(n):
        point = []
        for _ in range(3):
            point.append(random.gauss(0, 1))
        _array.append(point)
    return _array


ptCloud = point_cloud_generator(100000)
print("point cloud length: {}".format(len(ptCloud)))

# show the first 10 rows of the ptCloud 2d-array
pprint(ptCloud[:10])

ptCloud_np = np.asarray(ptCloud)

# finding the centroid of cloud of points
# since it was a random gaussian with mean 0, the center is very close to (0,0,0)
center = np.mean(ptCloud_np, axis=0)

# then calculating distances to centroid
distances = []
for row in ptCloud_np:
    distances.append(np.sqrt(np.sum((center - row)**2)))

print(f'Fitting sphere: radius {np.max(distances)} with center {center}')
