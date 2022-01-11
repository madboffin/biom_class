
import numpy as np

filename = "pointCloud.csv"

# code 
csv_values = np.genfromtxt(filename, delimiter=',')

# Test whether any array element along an axis evaluates to True
csv_values = csv_values[~np.isnan(csv_values).any(axis=1)]   

distance = np.sqrt(np.sum((csv_values)**2, axis=1))
mean_dist = np.mean(distance)
print(mean_dist)