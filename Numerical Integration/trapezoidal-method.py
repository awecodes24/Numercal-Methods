# To calculate integration of f(x)dx [a:b] by trapezoidal method

import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter lower limit: '))
b = float(input('Enter upper limit: '))
n = int(input('Enter the no. of partitions: '))

h = (b-a)/n

func = input('Enter the integrand function in terms of x using python syntax: ')
def f(x,func):
    return eval(func)
def y(x):
    return f(x, func)

x = np.linspace(a, b, n+1)

I = 0
s = 0
for i in range(1, n):
    s += y(x[i])

I = (h/2)*(y(x[0]) + 2 * s + y(x[n]))
print(f'The approximate integral is {I}')

plt.plot(x,[y(x) for x in x])
x_val = np.linspace(a-10, b+10, 1000)
plt.plot(x_val,[y(x) for x in x_val], label = func)
y_points = [y(x) for x in x]
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y_points[i], y_points[i+1], 0]
    plt.fill(xs, ys, color='pink', edgecolor = 'black', alpha = 0.2)
plt.grid(True)
plt.axhline(0, 0, color = 'green')
plt.axvline(0, 0, color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Trapezoidal Rule')
plt.show()