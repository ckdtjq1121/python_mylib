import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return np.log(x) / x


x = [f for f in range(1, 100)]

plt.plot(x, func(x))
plt.show()

