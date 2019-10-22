import matplotlib.pyplot as plt
import numpy as np

##plt.plot([1, 2, 3, 4, 5])
##plt.ylable('Some numbers')
##
##plt.show()

X = np.linspace(-np.pi * 1, np.pi * 1, 256, endpoint = True)
(C, S) = np.cos(X), np.sin(X)

fig = plt.figure(figsize=(10, 6), dpi = 80)

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'+$\pi/2$', r'+$pi$'])
plt.yticks([-1, 0, 1])


ax = plt.gca()
ax.spines['right'].set_color('blue')
ax.spines['top'].set_color('yellow')
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_color('red')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

t = 2 * np.pi/3

#for sine line
plt.plot([t, t], [0, np.sin(t)], color = 'green', lw=1, ls='--')
plt.scatter([t, ], [np.sin(t), ], 50, color = 'green')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{sqrt{3}}{2}$',
             xy = (t, np.sin(t)), xycoords='data',
             xytext = (+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

#for consine line
plt.plot([t, t], [0, np.cos(t)], color = 'blue', lw=1, ls='--')
plt.scatter([t, ], [np.cos(t), ], 50, color = 'blue')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy = (t, np.cos(t)), xycoords='data',
             xytext = (-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

plt.plot(X, C, 'b-', lw=2.5, label='cosine')
plt.plot(X, S, 'r-', lw=4.5, label='sine')

plt.legend(loc='upper left')

plt.show()
