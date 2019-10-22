import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 24, 1)
y = x - 9

plt.xticks(x)
plt.plot(x, y)
plt.show()
