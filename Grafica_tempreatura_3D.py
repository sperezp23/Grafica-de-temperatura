# %% Grafica 3D
import matplotlib.pyplot as plt
from matplotlib import cm, axis
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

sigma = 1
mu = 0
lim =4
liminf = 0

x = np.linspace(-lim,lim,100)
y = np.linspace(-lim,lim,100)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
# Z = 25+np.sinh(Y)-np.cosh(X)
Z = 25+np.sinh(Y)-np.cosh(X)

# Z = Y
# Z = (1/np.sqrt(2*np.pi*sigma))*np.exp(-(X**2 + Y**2)/(2*sigma**2)

ax.plot_surface(X, Y, Z,cmap=cm.jet,vmax=Z.max(),vmin=Z.min())
fig.set_size_inches(10,10)
plt.show()
