"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
from __future__ import print_function
import random
import datetime
# seeding the random number generator
random.seed(datetime.datetime.now().year)

spectrum = ['violet', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']

rnd_seq = [random.choice(spectrum) for _ in range(100000)]

item_idxs = [k for k, item in enumerate(rnd_seq) if (item == 'blue')]

print(item_idxs)
