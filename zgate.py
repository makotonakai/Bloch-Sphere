# Remove the # below if you are using Jupyter Notebook.
#%matplotlib nbagg

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
zgate_theta = np.linspace(theta,theta,number)
zgate_phi = np.linspace(phi,phi+np.pi,number)
# The array of all the coordinates in each moment
zgate = []
#The array of each coordinate in each moment
zgate_x = []
zgate_y = []
zgate_z = []
for i in range(number):
    zgate_x.append(np.sin(zgate_theta[i]) * np.cos(zgate_phi[i]))
    zgate_y.append(np.sin(zgate_theta[i]) * np.sin(zgate_phi[i]))
    zgate_z.append(np.sqrt(1-np.sqrt(zgate_x[i]**2+zgate_y[i]**2)))
for j in range(number):        
    arrow = plt.quiver(0,0,0,zgate_x[j],zgate_y[j],zgate_z[j],color="red")
    zgate.append([arrow])
ani = animation.ArtistAnimation(fig,zgate,interval=100)
plt.show()