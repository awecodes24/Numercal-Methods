# To solve initial value problem of 1st order by RK-4 method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode = input('Enter dy/dx in terms of x and y using python syntax: ')
def F(x, y, ode):
    return eval(ode)
def f(x,y):
    return F(x, y, ode)

x = float(input('Enter the initial value of x: '))
y = float(input('Enter the initial value of y: '))
h = float(input('Enter the step-length: '))
n = int(input('Enter the number of steps: '))

t = []
xval = []
yval = []

for i in range(n):
    k1 = h * f(x,y)
    k2 = h * f(x+h/2, y+k1/2)
    k3 = h * f(x+h/2, y+k2/2)
    k4 = h * f(x+h, y+k3)
    y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    x = x + h
    t.append([x,y])
    xval.append(x)
    yval.append(y)

t = pd.DataFrame(t, columns= ['x', 'y'])
print("Solutions: ")
print(t)
plt.plot(xval, yval, label = ode)
plt.grid(True)
plt.title('RK-4 Method')
plt.show()
