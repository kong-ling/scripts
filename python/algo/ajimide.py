import numpy as np  #阿基米德螺线
import matplotlib.pyplot as plt
#Numpy 中 arange() 主要是用于生成数组 具体用法如下:
#numpy.arange(start stop step  dtype = None)
#start 开始位置 数字，可选项 默认起始值为0
#stop 停止位置 数字
#step 步长 数字 可选项 默认步长为1 如果指定了step 则还必须给出start
#dtype 输出数组的类型 如果未给出dtype 则从其他输入参数推断数据类型
t = np.arange(-3*np.pi,3*np.pi,0.01)
x = t*np.cos(t)
y = t*np.sin(t)
plt.title(r"$\rho=a\theta\quad a=1$")
plt.plot(x,y)
plt.grid()
plt.show()
