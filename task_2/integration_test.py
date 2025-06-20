import scipy.integrate as spi
import numpy as np

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return np.sin(x**2) + np.log(x + 1)

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 3  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)
