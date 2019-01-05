# Remove the # below if you are using Jupyter Notebook.
#%matplotlib nbagg

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

print("Put angle theta and phi, 0≤ theta ≤180, 0≤ phi ≤360")
theta = input("theta:")
phi = input("phi:")
theta = np.radians(float(theta))
phi = np.radians(float(phi))
X = np.sin(theta) * np.cos(phi)
Y = np.sin(theta) * np.sin(phi)
Z = np.cos(theta)

# If the length of vector is more than 1, I divides each coordinate by its original length.
length = np.sqrt(X**2 + Y**2 + Z**2)
if length > 1:
    X = X/length
    Y = Y/length
    Z = Z/length

# Figure of the animation   
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(x,y,z, color="black")

# Number of moments on the animation    
number = 10
# The value of theta, phi in each moment
xgate_theta = np.linspace(theta,theta+np.pi,number)
xgate_phi = np.linspace(phi,phi,number)
# The array of all the coordinates in each moment
xgate= []
#The array of each coordinate in each moment
xgate_x = []
xgate_y = []
xgate_z = []
for i in range(number):
    xgate_x.append(X)
    xgate_z.append(np.cos(xgate_theta[i]))
    xgate_y.append(np.sqrt(1-np.sqrt(xgate_x[i]**2+xgate_z[i]**2))*(-1))
    
for j in range(number):        
    arrow = plt.quiver(0,0,0,xgate_x[j],xgate_y[j],xgate_z[j],color="red")
    xgate.append([arrow])
    
ani = animation.ArtistAnimation(fig,xgate,interval=1000)
plt.show()