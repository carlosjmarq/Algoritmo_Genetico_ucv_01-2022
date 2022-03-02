import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from algoritmo import f1
import numpy as np
import time


x = np.linspace(-10,10,int(20/0.005))
y = np.linspace(-10,10,int(20/0.005))
X,Y = np.meshgrid(x,y)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X,Y,f1(X,Y))

plt.show()