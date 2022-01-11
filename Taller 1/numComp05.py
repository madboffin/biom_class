"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
from __future__ import print_function
import numpy as np
import pandas as pd
# print(datetime.datetime.now().year)

f = open('coordinates.csv', 'r')
lines = f.readlines()
f.close()

csv_values_list = []
for k, line in enumerate(lines):
    if k == 0:continue                 # skipping first line
    if "\n" in line:
        line = line.replace('\n', '')  # removing \n characters
    csv_values_list.append(line.split(','))

csv_values = np.asarray(csv_values_list).astype(float)
csv_r = csv_values[:, :3]
csv_l = csv_values[:, 3:]
mean_dist = np.mean(np.sqrt(np.sum((csv_l - csv_r)**2, axis=1)))
print(mean_dist)


# another way, with pandas
df = pd.read_csv('coordinates.csv')
# print(df.head())
csv_r = df.filter(regex=r'r.').to_numpy()
csv_l = df.filter(regex=r'l.').to_numpy()
mean_dist_p = np.mean(np.sqrt(np.sum((csv_l-csv_r)**2, axis=1)))
print(mean_dist_p)
