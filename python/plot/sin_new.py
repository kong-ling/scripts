import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = x
y5 = np.exp(x)

plt.axis([-np.pi, np.pi, -1.5, 1.5])
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([i * np.pi/2 for i in range(-4, 5)], [str(i*0.5)+'$\pi$' for i in range(-4, 4)])
plt.plot(x, y1, color='r', linestyle='--', linewidth=1)
plt.plot(x, y2, color='y', linestyle='--', linewidth=1)
#plt.plot(x, y3, color='g', linestyle='--', linewidth=1)
plt.plot(x, y4, color='b', linestyle='--', linewidth=1)
plt.plot(x, y5, color='c', linestyle='--', linewidth=1)
#plt.plot(x, t, color='m', linestyle='--', linewidth=1)

#plt.show()
plt.savefig('sin.png', dpi=120)
