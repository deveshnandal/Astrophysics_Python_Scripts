### Fractal generation from chat



import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter, threshold):
    z = 0
    n = 0
    while abs(z) <= threshold and n < max_iter:
        z = z*z + c
        n += 1
    return n

xmin, xmax, ymin, ymax = -2, 0.5, -1.25, 1.25
width, height, max_iter, threshold = 1000, 1000, 500, 2

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = np.array([[mandelbrot(complex(r, i), max_iter, threshold) for r, i in zip(row, col)] for row, col in zip(X, Y)])

plt.imshow(Z, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.show()
