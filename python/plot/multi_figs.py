import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.1)
y1= np.exp(x)
y2= np.exp(1.5*x)
y3= np.exp(2*x)

plt.figure(1)
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='r')

plt.xlabel('x')
plt.ylabel('y1=exp(x)')

plt.figure(2)
plt.subplot(2, 2, 3)
plt.plot(x, y2, color='b')
plt.savefig('exp1.5.png', dpi=120)

plt.xlabel('x')
plt.ylabel('y2=exp(1.5x)')

plt.figure(1)
plt.subplot(2, 2, 2)
plt.plot(x, y3, color='y')

plt.xlabel('x')
plt.ylabel('y3=exp(2x)')

plt.savefig('exp.png', dpi=120)
plt.show()
