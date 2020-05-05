import numpy as np
import matplotlib.pyplot as plt


<<<<<<< HEAD
def plot3D():
   ##### this plots the temperature vs time data as a surface
   fig1 = plt.figure()
   ax = fig1.add_subplot(111, projection='3d')
   foo = ax.plot_surface(X*100, TIME, T)
   ax.set_xlabel('x (cm)')
   ax.set_ylabel('time (Seconds)')
   ax.set_zlabel('temperature (deg C)')
   ##for i in range(5):
   ##   plt.plot(T[:,i])
   plt.show()
   return 
=======
>>>>>>> 9d7e1548e78c70c7d20eb364ca698c440dc28b99

A = 1 # cross sectional area of wall element in m^2
rho = 120.0 # density of wall material in kg / m^3
k = 0.038 # thermal conductivity of wall material in W / (m*C)
c = 700.0 # specific heat capacity in J / (kg*C)
h = 20.0 # convective heat transfer coefficient in W / (m^2 * C)
T_initial = 20.0 # initial temperature in deg c
T_room = 12.0 # ambient temperature in deg c
T_out_amb = 27.0 # ambient temperature in deg c
L = 0.15 # thickness of the entire wall in meters
Q_dot = 650.0 # Solar Radiation in watts/sqm
N = 5 # number of discrete wall segments, so points will be N+1 (0,1,2,3,...,N)
dx = L/N # length of each wall segment in meters
total_time = 300.0 # total duration of simulation in seconds
nsteps = 10 # number of timesteps
dt = total_time/nsteps # duration of timestep in seconds
alpha = k/(rho*c) # Thermal diffusivity
fou =  alpha * dt /(dx*dx)         #(k*dt) / (c*rho*dx*dx) Fourier number 
heatfac = dx / (k*A) # heat fraction

print ("dt",dt)
print ("fou",fou)

assert fou < 0.5 # Stability Criteria
   
   

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

for j in range(len(timesamps)-1):
#for j in range(5):
   T_out = T[0, j]
   #Node 0
   T[0, j+1] = T[0,j] + fou* (T[1,j] - T[0,j] + heatfac * Q_dot- heatfac*h*A*(T_out - T_out_amb))
   #T[0, j+1] = 27 # if fixed boundary condition
   #  (last Node)
   T_in = T[len(x)-1, j]
   T[len(x)-1, j+1] = T_in + fou * (T[len(x)-2, j] - T_in) - fou*heatfac*h*A*(T_in - T_room)
   #T[len(x)-1, j+1] = 12 # if fixed boundary condition
   #interior elements 
   for i in range(len(x)-2):
      T[i+1,j+1] = T[i+1,j] + fou * (T[i,j] - 2*T[i+1,j] + T[i+2,j])
   print ("Intermidiate T\n",T)   

print ("Final T\n",T)


<<<<<<< HEAD

=======
## Plot 
>>>>>>> 9d7e1548e78c70c7d20eb364ca698c440dc28b99

masterlist = []
for i in range(10):
   masterlist.append(T[:,i])
<<<<<<< HEAD


print ("masterlist",masterlist)
##
###plt.figure(figsize=(6.0, 4.0))

##
i=-1
for impacts in masterlist:
    i=i+1
    plt.plot(impacts,label="{} x {} sec".format(i,dt))
    plt.legend()

#pyplot.xlim(0.0, L)
=======
   
print ("masterlist",masterlist)

i=-1
for impacts in masterlist:
    i=i+1
    
    plt.plot(impacts,label="{} x {} sec".format(i,dt))
    plt.legend()

#ply.xlim(0.0, L)
>>>>>>> 9d7e1548e78c70c7d20eb364ca698c440dc28b99
#pyplot.ylim(0.0, 100.0);
plt.xlabel('Node')
plt.ylabel('Temperature [C]')
plt.grid()
plt.show()

