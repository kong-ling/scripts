import numpy as np
import matplotlib.pyplot as plt
alpha = 1
#numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#start    序列的起始值
#stop    序列的终止值，如果endpoint为true，该值包含于数列中
#num    要生成的等步长的样本数量，默认为50
#endpoint    该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
#retstep    如果为 True 时，生成的数组中会显示间距，反之不显示。
#dtype    ndarray 的数据类型
theta = np.linspace(0,2*np.pi,num=500)
x = alpha * np.sqrt(2) * np.cos(theta) / (np.sin(theta)**2+1)
y = alpha * np.sqrt(2) * np.cos(theta) * np.sin(theta)/(np.sin(theta)**2+1)
plt.title(r"$\rho^{2}=a^{2}\cos 2\theta\quad a=1$")
plt.plot(x,y)
plt.grid()
plt.show()
