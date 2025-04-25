#from scipy import random
import numpy as np
import sympy as sym
#from scipy.integrate import quad as integrate

#limites de integracion
a=0
b=1
c = -3
d = 3

N=100000

#arreglo de ceros de longitud N
arry=np.zeros(N)

# iterando sobre cada valor de el arreglo
# llenando con valores aleatorios el intervalo entre a y b
np.random.seed(10)
for i in range(N):
  arry[i]=np.random.uniform(a,b)

integral1=0.0
for i in range(N):
  integral1+=(1+arry[i]**2)*np.sin(5 * np.pi * arry[i])+8/5

#Integral por el metodo montecarlo
integral1=(b-a)/N*integral1

for i in range(N):
  arry[i]=np.random.uniform(c,d)

integral2 = 0.0
for i in range(N):
  integral2+=np.exp(-arry[i]**2-np.sin(2*arry[i])**2)

integral2=(d-c)/N*integral2

print("Integral 1 por montecarlo",integral1)

print("Integral 2 por montecarlo",integral2)

#Integral verdadera

x=sym.Symbol('x')
f = (1 + x**2)*sym.sin(5 * sym.pi * x) + 8/5
g = sym.exp(-x**2-sym.sin(2*x)**2)

print("Valor real de la integral 1",sym.integrate(f, (x, a, b)))
print("Valor real de la integral 2",sym.integrate(g, (x, c, d)))