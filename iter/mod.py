import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)

plt.plot(x, y_sin)
print(__name__)

if __name__ == '__main__':
    plt.show()
