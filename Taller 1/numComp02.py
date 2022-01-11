"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
from __future__ import print_function
import random
import datetime

# seeding the random number generator
random.seed(datetime.datetime.now().year)

rnd_seq = [random.choice([False, True])
           for _ in range(100000)]

print(len(rnd_seq))

cnt = 0

# from second item to end
for k in range(1, len(rnd_seq)):
    # adds to counter if false is followed by true
    if (not rnd_seq[k-1] and rnd_seq[k]):
        cnt += 1
print(cnt)
