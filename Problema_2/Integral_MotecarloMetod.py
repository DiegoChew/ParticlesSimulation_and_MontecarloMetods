#from scipy import random
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
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

f_np = sym.lambdify(x, f, 'numpy')
g_np = sym.lambdify(x, g, 'numpy')


x1_vals = np.linspace(a, b, 1000)
x2_vals = np.linspace(c, d, 1000)


y1_vals = f_np(x1_vals)
y2_vals = g_np(x2_vals)


fig, axs = plt.subplots(2, 1, figsize=(8, 6))

axs[0].plot(x1_vals, y1_vals, label='f(x)')
axs[0].set_title("f(x) = (1 + x²)sin(5πx) + 8/5")
axs[0].grid(True)
axs[0].legend()

axs[1].plot(x2_vals, y2_vals, color='orange', label='g(x)')
axs[1].set_title("g(x) = exp(-x² - sin²(2x))")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()