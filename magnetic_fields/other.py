import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 60)
y = np.linspace(-1, 1, 60)

def f(x, y):
    return np.sin(x) + 2*np.cos(6*y)

z = np.array([f(i, j) for j in y for i in x])

X, Y = np.meshgrid(x, y)
Z = z.reshape(60, 60)

plt.pcolor(X, Y, Z)
plt.show()