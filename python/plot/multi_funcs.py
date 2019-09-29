import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.1)
y1= np.exp(x)
y2= np.exp(1.5*x)
y3= np.exp(2*x)

plt.plot(x, y1, color='r')

plt.plot(x, y2, color='b')

plt.plot(x, y3, color='y')

#plt.axis([0, 1])
plt.title('exp for different exponient')

plt.savefig('mul_exp.png', dpi=120)


timetable = range(24)
timetable_sandiego = [x - 15 for x in timetable]




plt.show()
