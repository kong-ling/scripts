#<<<<<<< HEAD
#import numpy as np
#import matplotlib.pyplot as plt
#X = np.linspace(-np.pi, np.pi, 256)
#plt.plot(X, np.cos(X))
#plt.plot(X, np.sin(X))
#
#plt.show()
#=======
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
#the height function
    return(1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n=256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)

#use plt.contourf to filling contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha = 0.75, cmap = plt.cm.hot)

#use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors = 'black', linewidth = 0.5)

plt.clabel(C, inline = True, fontsize = 10)

plt.xticks(())
plt.yticks(())
plt.show()

#>>>>>>> 12bb23d86a12f1c17a463d0b319dad9655366fd0
