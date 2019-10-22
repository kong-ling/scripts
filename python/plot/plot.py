import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256)
plt.plot(X, np.cos(X))
plt.plot(X, np.sin(X))

plt.show()
