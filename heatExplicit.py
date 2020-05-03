import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

A = 1 # cross sectional area of wall element in m^2
rho = 120.0 # density of wall material in kg / m^3
k = 0.38 # thermal conductivity of wall material in W / (m*C)
c = 700.0 # specific heat capacity in J / (kg*C)
h = 20.0 # convective heat transfer coefficient in W / (m^2 * C)

T_initial = 23.0 # initial temperature in deg c
T_room = 12.0 # ambient temperature in deg c
T_out_amb = 35.0 # ambient temperature in deg c


L = 0.15 # thickness of the entire wall in meters
N = 5 # number of discrete wall segments
dx = L/N # length of each wall segment in meters

total_time = 3600.0 # total duration of simulation in seconds
nsteps = 100 # number of timesteps
dt = total_time/nsteps # duration of timestep in seconds
print ("dt",dt)

simfac = (k*dt) / (c*rho*dx*dx)
print ("simfrac",simfac)

heatfac = dx / (k*A)

# initialize volume element coordinates and time samples
x = np.linspace(0, dx*(N-1), N)
timesamps = np.linspace(0, dt*nsteps, nsteps+1)

X, TIME = np.meshgrid(x, timesamps, indexing='ij')

print ("X",X)

print ("Time",TIME)



T = np.zeros((X.shape))

print ("T",T)

for i in range(len(x)):
   T[i, 0] = T_initial
##
print ("Initial T",T)
##
Q_dot_in = 650.0 # Solar Radiation in watts
##
for j in range(len(timesamps)-1):
#for j in range(5):
   T_out = T[0, j]
   # and now compute temperature at the outside boundary for the next time step (Node 0)
   T[0, j+1] = T[0,j] + simfac * (T[1,j] - T[0,j] + heatfac * Q_dot_in- heatfac * h * A * (T_out - T_out_amb))
   #T[0, j+1] = 35
   # get the inside wall temperature (last Node)
   T_in = T[len(x)-1, j]
   # now compute temperature at the indside room boundary for the next time step
   T[len(x)-1, j+1] = T_in + simfac * (T[len(x)-2, j] - T_in - heatfac * h * A * (T_in - T_room))
   #T[len(x)-1, j+1] = 12 
   # now loop through the interior elements to get their temp for the next time
   for i in range(len(x)-2):
      T[i+1,j+1] = T[i+1,j] + simfac * (T[i,j] - 2*T[i+1,j] + T[i+2,j])
   print ("Intermidiate T\n",T)   

print ("Final T\n",T)
### this plots the temperature vs time data as a surface
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
foo = ax.plot_surface(X*100, TIME, T)
ax.set_xlabel('x (cm)')
ax.set_ylabel('time (Seconds)')
ax.set_zlabel('temperature (deg C)')
##for i in range(5):
##   plt.plot(T[:,i])
plt.show()


