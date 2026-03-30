# To find Lagrange interpolation polynomial for the given data

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input("Enter the no. of data points: "))
X = np.array(list(map(float, input("Enter all x-data: ").split())))
Y = np.array(list(map(float, input('Enter all y-data: ').split())))

print('Data points are: ')
for i in range(n):
    print(f'({X[i]}, {Y[i]})')

x = sp.symbols('x')
poly = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if j != i:
            lf *= (x - X[j])/(X[i] - X[j])
    
    poly += Y[i] * lf


poly = sp.simplify(poly)
print('The lagrange polynomial is: \n', poly)

xp = float(input('Interpolation point: '))
int_val = poly.subs(x, xp)
print(int_val)
f = sp.lambdify(x, poly, 'numpy')
x_val = np.linspace(-10, 10, 1000)
plt.plot(x_val,f(x_val),color='r',label='Polynomial')
plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.xlabel('x_val')
plt.ylabel('f(x_val)')
plt.legend()
plt.grid(True)
plt.scatter(xp,int_val, color = 'g', zorder = 5)
plt.show()

