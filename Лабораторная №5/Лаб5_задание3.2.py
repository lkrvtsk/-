import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
def func1(x,y):
    return np.power(x, 1/4) + np.power(y, 1/4)

def func2(x,y):
    return x**2 - y**2

def func3(x,y):
    return 2*x + 3*y

def func4(x,y):
    return x ** 2 + y ** 2

def func5(x, y):
    return 2 + 2*x + 2*y - x**2 - y**2

def plot_function(func, title):
    z = func(*np.meshgrid(x, y))
    #plt.contourf(x, y, z, levels=20, cmap='viridis')
    #plt.colorbar()
    plt.plot(x, z)
    plt.title(title)
    plt.show()

plot_function(func1, 'z=x^(1/4)+y^(1/4)' )
plot_function(func2, 'z=x^2-y^2')
plot_function(func3, 'z=2x+3y')
plot_function(func4, 'z=x^2+y^2')
plot_function(func5, 'z=2+2x+2y-x^2-y^2')
