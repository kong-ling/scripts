import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_sin2x = np.sin(2 * x)
y_cos2x = np.cos(2 * x)

plt.subplot(2, 2, 1)
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(2, 2, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.subplot(2, 2, 3)
plt.plot(x, y_sin2x)
plt.title('Sine2x')

plt.subplot(2, 2, 4)
plt.plot(x, y_cos2x)
plt.title('Cosine2x')

plt.show()
