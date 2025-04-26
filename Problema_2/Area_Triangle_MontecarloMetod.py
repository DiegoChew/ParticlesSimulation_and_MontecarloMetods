import random
import numpy as np
import matplotlib.pyplot as plt

num_points = 1000000
points_inside_triangle = 0 
# rndm_seed=random.seed(100) 

y_in=[]
x_in=[]

y_out=[]
x_out=[]


for i in range(num_points):
    r1 =  np.sqrt(random.uniform(0, 1)) 
    theta = random.uniform(-np.pi/2,np.pi/2) 
    x = r1 * np.cos(theta)
    y = r1 * np.sin(theta)+1

    if  y > np.sqrt(3)*x and y < 1.5: 
        points_inside_triangle += 1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)

plt.scatter(x_out,y_out,color='red',marker='*', alpha=0.1)        
plt.scatter(x_in,y_in,color='blue', marker="+", alpha=0.1)
# plt.scatter(x_out,y_out,color='red',marker='*', alpha=0.1)
plt.show()

print(np.pi*points_inside_triangle/num_points)