import numpy as np

x = 0.24
a = 5.8

z = np.arctan(x**2) + (np.cos(np.pi/2-a))**3 / np.abs(x-a**0.2)

print(z)

