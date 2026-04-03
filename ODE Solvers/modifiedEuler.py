# To solve initial value problem of 1st order by Euler's method

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
    y_predict = y + h* f(x,y)
    y_correct = y + (h/2) * (f(x,y) + f(x+h,y_predict))
    y = y_correct
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