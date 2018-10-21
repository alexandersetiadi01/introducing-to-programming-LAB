import numpy as np
import matplotlib.pylab as plt
import math as m

vo = int(input("velocity = "))
a = float(input("angle degree = "))
g = 9.81

theta = np.radians(a)
t_max = 2*(vo*m.sin(theta)/g)
t = np.linspace(0, t_max, num=1000) # Set time as 'continous' parameter.

x1 = []
y1 = []
for k in t:
    x = ((vo*k)*np.cos(theta)) # get positions at every point in time
    y = ((vo*k)*np.sin(theta))-((0.5*g)*(k**2))
    x1.append(x)
    y1.append(y)
p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor
for i in sorted(p, reverse=True):
    del x1[i]
    del y1[i]

plt.plot(x1, y1) # Plot for every angle

plt.title("Projectile Motion", fontsize=13, color="purple")
plt.ylabel("y-coordinate", fontsize=10, color="red")
plt.xlabel("x-coordinate", fontsize=10, color="blue")

plt.show() # And show on one graphic
