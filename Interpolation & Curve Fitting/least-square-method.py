# To fit a second degree curve y = a + bx + cx**2 to the given data using least square method

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import numpy.linalg as slg

n = int(input("Enter the no. of data points: "))
X = np.array(list(map(float, input("Enter all x-data: ").split())))
Y = np.array(list(map(float, input('Enter all y-data: ').split())))

A = [[n, np.sum(X), np.sum(X**2)], [np.sum(X), np.sum(X**2), np.sum(X**3)], [np.sum(X**2), np.sum(X**3), np.sum(X**4)]]
B = [[np.sum(Y)], [np.sum(X*Y)], [np.sum(X**2 * Y)]]

print('The coefficient matrix of system of normal equation:\n', np.matrix(A))
print('The output matrix of system of normal equation:\n', np.matrix(B))

coeff = slg.solve(A,B)
print(f'The curve of best fit is {coeff[0]} + {coeff[1]}x + {coeff[2]}x**2')

x = np.linspace(min(X)-2, max(X)+2, 1000)
plt.plot(x, coeff[0]+ coeff[1]*x + coeff[2]*x**2, label="Best Fit Curve")
plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.scatter(X, coeff[0]+ coeff[1]*X + coeff[2]*X**2, color = 'g', zorder = 5)
plt.show()

# 1 2 3 4 5
# 1090 1220 1390 1625 1925