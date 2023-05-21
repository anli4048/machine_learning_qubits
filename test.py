#import scqubits.testing as sctest
#sctest.run()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1.,1.,0.05)
y = np.arange(-1.,1.,0.05)

fig = plt.figure()
ax = plt.axes(projection='3d')
xg,yg = np.meshgrid(x, y)
ax.plot_surface(xg,yg, xg*xg+yg*yg)
plt.xlabel("x (GHz)")
plt.ylabel("y (GHz)")
plt.title("f(x,y) (us)")