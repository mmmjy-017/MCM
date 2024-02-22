import numpy as np

x0 = np.arange(0, 2.2, 0.3)
x0*=1852;
beta = np.arange(0, 316, 45)  # 这里用316确保包含315
beta = np.deg2rad(beta)
alpha = 1.5*np.pi/180
theta = 120*np.pi/180

x0, beta = np.meshgrid(x0, beta)
a = -np.cos(beta)*np.sqrt(1 / (np.cos(alpha)**2) - 1)
b = np.sqrt((1 - np.cos(beta)**2) * (1 - np.cos(alpha)**2) / (np.cos(alpha)**2))
c = -110

y1 = (a*x0 + c) / (1/np.tan(theta/2) - b)
y2 = -(a*x0 + c) / (1/np.tan(theta/2) + b)
z1 = (a*x0 + c) / (1 - b*np.tan(theta/2))
z2 = (a*x0 + c) / (1 + b*np.tan(theta/2))

d = np.sqrt((y1-y2)**2 + (z1-z2)**2)

print(d)

np.savetxt('output_data.csv', d, delimiter=',')

#
#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#
## Data
#distance = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1])  # 海里
#angle = np.array([0, 45, 90, 135, 180, 225, 270, 315])  # degrees
#
#depth_values = np.array([
#    # 详见参考文献
#])
#
## Plotting
#fig = plt.figure(figsize=(10, 8))
#ax = fig.add_subplot(111, projection='3d')
#
#X, Y = np.meshgrid(angle, distance)
#ax.plot_surface(X, Y, depth_values, cmap="viridis")
#
#ax.set_xlabel('Angle (°)')
#ax.set_ylabel('Distance (nautical miles)')
#ax.set_zlabel('Depth (m)')
#ax.set_title('Depth vs Distance and Angle')
#plt.show()