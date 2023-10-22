import numpy as np
import matplotlib.pyplot as plt


a_values = (0, 2, 0.2)

arg_values = []
func_values = []

for a in a_values:
    x = 12.1
    func_value = np.exp(a * x) - 3.45 * a
    arg_values.append(x)
    func_values.append(func_value)

arg_values = np.array(arg_values)
func_values = np.array(func_values)

max_value = func_values.max()
min_value = func_values.min()
mean_value = func_values.mean()
num_elements = func_values.size

print("max: ", max_value)
print("min: ", min_value)
print("mean: ", mean_value)
print("quantity: ", num_elements)

plt.plot(a_values, func_values, 'o-', label='f(x)')
plt.axhline(mean_value, color='r', linestyle='--', label='mean')

plt.xlabel('a')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('изменение ф-ции ')
plt.show()
