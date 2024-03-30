# %% Mapa de calor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

x = np.linspace(-1,1,500)
y = np.linspace(-1,1,500)
X,Y = np.meshgrid(x, y)
Z = 25+np.sinh(Y)-1.618*np.cosh(X)

fig, ax = plt.subplots()
ax.imshow(Z,cmap=cm.jet,vmin=Z.min(),vmax=Z.max())
fig.set_size_inches(8,8)
