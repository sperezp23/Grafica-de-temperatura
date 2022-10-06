# # %% Grafico de ensayo 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

x = np.linspace(-1,1,500)
y = np.linspace(-1,1,500)
X,Y = np.meshgrid(x, y)
Z = 25+np.sinh(Y)-1.618*np.cosh(X)

fig, ax = plt.subplots()
ax.imshow(Z,cmap=cm.jet,vmin=Z.min(),vmax=Z.max())

# %% Grafico de temperatura con Excel
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

datos = pd.read_excel('Libro1.xlsx',sheet_name=2)
z= np.array("Temp")
plt.contourf(x,y,z)
# fig, ax = plt.subplots()
# ax.imshow(Z,cmap=cm.jet,vmin=Z.min(),vmax=Z.max())