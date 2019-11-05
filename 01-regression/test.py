import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = 'Simhei'  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 解决显示问题

x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
x_d = np.asarray(x_data)
y_d = np.asarray(y_data)

# 生成模型
x = np.arange(-200, -100, 1) # b
y = np.arange(-5, 5, 0.1) # w
Z = np.zeros((len(x), len(y)))
X, Y = np.meshgrid(x, y)  # 网格图
# plt.plot(X,Y,marker='.',linestyle='')
# plt.show()

# 得到loss数组Z
for i in range(len(x)):
	for j in range(len(y)):
		b = x[i]
		w = y[j]
		for n in range(len(x_data)):
			Z[j][i] += (y_data[n] - b - w * x_data[n]) ** 2
	Z[j][i] /= len(x_data)

fig = plt.figure()
ax = fig.gca(projection='3d')
 
ax.plot_surface(Y, X, Z, cmap=plt.get_cmap('rainbow'))
# ax.contourf(Y, X, Z ,zdir='Z', cmap='rainbow')

plt.show()
