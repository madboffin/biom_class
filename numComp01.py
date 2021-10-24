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

item_idxs = []

for i in range(0,len(rnd_seq)):
     if  rnd_seq[i]=='blue':
         item_idxs.append(i)
         


 
print('-'*30)
print("SOLUTION NCP01-P1")
print("Los indices son")

# TODO  realizar la solución al problema



print (item_idxs)
print('-'*30)