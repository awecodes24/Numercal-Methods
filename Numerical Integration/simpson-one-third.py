# To calculate integration of f(x)dx [a:b] by Simpson 1/3rd method

import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter lower limit: '))
b = float(input('Enter upper limit: '))
n = int(input('Enter the no. of partitions in multiple of 2: '))

if( n%2 != 0):
    print('The partitions must be multiple of 2.')

else:

    h = (b-a)/n

    func = input('Enter the integrand function in terms of x using python syntax: ')
    def f(x,func):
        return eval(func)
    def y(x):
        return f(x, func)

    x = np.linspace(a, b, n+1)

    I = 0
    s1 = 0
    s2 = 0
    for i in range(1, n):
        if i%2 != 0:
            s1 += y(x[i])
        else:
            s2 += y(x[i])

    I = (h/3)*(y(x[0]) + 4 * s1 + 2 * s2 + y(x[n]))
    print(f'The approximate integral is {I}')

    plt.plot(x,[y(x) for x in x])
    x_val = np.linspace(a-10, b+10, 1000)
    plt.plot(x_val,[y(x) for x in x_val], label = func)
    y_points = [y(x) for x in x]
    for i in range(0, n, 2):
        xs = x[ i: i + 3]
        ys = y_points[i : i + 3]
        plt.fill_between(xs, ys, color='pink', edgecolor = 'black', alpha = 0.2)
    plt.grid(True)
    plt.axhline(0, 0, color = 'green')
    plt.axvline(0, 0, color='green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Simpson 1/3rd Rule')
    plt.show()