import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 10*np.sin(0.3*x)*np.sin(1.3*x**2)+0.001*x**4+0.2*x+80  

def distribution(x, beta):
    return np.exp(-beta * f(x))

beta = 5.0      
sigma = 0.5    
iterations = 1000000
ignore = 100000  

x_current = 0  
points = []    


for i in range(iterations):

    x_proposed = x_current + np.random.normal(0, sigma)
    alpha = min(1, distribution(x_proposed, beta) / distribution(x_current, beta))
    
    if np.random.uniform(0, 1) < alpha:
        x_current = x_proposed 
    points.append(x_current)


points = points[ignore:]  
x_min = np.mean(points[-1000:]) 

print(f"Mínimo estimado: x = {x_min:.3f}")

