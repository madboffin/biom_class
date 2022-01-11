"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
from __future__ import print_function
from pprint import pprint
import random
import datetime
import numpy as np

# seeding the random number generator
N = 100000
random.seed(datetime.datetime.now().year)

x_array = []
for row in range(N):
    point = []
    for i in range(3):
        point.append(random.random())
    x_array.append(point)

# show the first 10 rows of the X array
pprint(x_array[:10])

# a faster way
x_sqrt = np.asarray(x_array)**2
x_leng = np.sqrt(np.sum(x_sqrt, axis=1))

# another way
x_leng = []
for row in x_array:
  x_leng.append(np.sqrt(row[0]**2 + row[1]**2 + row[2]**2))

print(x_leng)