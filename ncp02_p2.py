
import numpy as np

filename = "pointCloud.csv"

# TODO: add your code here
data = genfromtxt(filename, delimiter=',')
data = data[~np.isnan(data)]

data= np.reshape(data, (-1, 3))
x = data[:,0]
y = data[:,1]
z = data[:,2]


vec_distancias=[]
for t in range (0,len(data)):
    distancia = ((x[t])**2+(y[t])**2+(z[t])**2)**(1/2)
    vec_distancias.append(distancia)

promedio = np.mean(vec_distancias)        
print (promedio)
