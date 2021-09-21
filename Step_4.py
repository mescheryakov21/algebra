
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def f(p):
    x, y = p
    return (x ** 2 - 1 - y), (np.exp(x) + x - x * y - 1)

x = np.linspace(-2, 5, 200)
x1 = fsolve(f, (-2, 5))
x2= fsolve(f, (-2, 5))
x3= fsolve(f, (-2, 5))
print(x1)
print(x2)
print(x3)
plt.plot(x, x ** 2 - 1)
plt.plot(x, (np.exp(x)-1)/x + 1)
plt.ylim(-1, 15)
plt.grid(True)

plt.show()