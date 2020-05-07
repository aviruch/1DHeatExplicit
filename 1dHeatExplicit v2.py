import numpy as np
import matplotlib.pyplot as plt

A = 1 # cross sectional area of wall element in m^2
rho = 120.0 # density of wall material in kg / m^3
k = 0.038 # thermal conductivity of wall material in W / (m*C)
c = 700.0 # specific heat capacity in J / (kg*C)
h = 15.0 # convective heat transfer coefficient in W / (m^2 * C)
T_initial = 20.0 # initial temperature in deg c
T_room = 12.0 # ambient temperature in deg c
T_out_amb = 27.0 # ambient temperature in deg c
L = 0.15 # thickness of the entire wall in meters
Q_dot = 650.0 # Solar Radiation in watts/sqm
N = 5 # number of discrete wall segments, so points will be N+1 (0,1,2,3,...,N)
dx = L/N # length of each wall segment in meters
#total_time = 300.0 # total duration of simulation in seconds
nsteps = 10 # number of timesteps
#dt = total_time/nsteps # duration of timestep in seconds
dt = 60 # sec
alpha = k/(rho*c) # Thermal diffusivity
fou =  alpha * dt /(dx*dx)         #(k*dt) / (c*rho*dx*dx) Fourier number 
heatfac = dx / (k*A) # heat fraction

print ("dt",dt)
print ("fou",fou)

assert fou < 0.5 # Stability Criteria

# initialize volume element coordinates and time samples
x = np.arange(0,L+dx,dx)
print ("x",x)
timesamps = np.arange(0, dt*nsteps+dt, dt)
print ("timestep",timesamps)

#Empty list
T = []
# Create 2D array of time and nodes (List of List)
for time in range(len(timesamps)):
    T.append([])    
    for node in range(len(x)):
        T[time].append(node)
        
       
# Converting list to numpy array         
T = np.array(T,dtype=float)

# Assign all points T_initial        
for time in range(len(timesamps)):    
    for node in range(len(x)):
        T[time,node] =  T_initial       
        
#T = np.array([[20 for i in range(len(x))] for j in range(len(timesamps))],dtype=float )
# # in T rows are time and columns are space nodes.
print("Initial 2D array where each row is time and columns are nodes\n",T)

for j in range(len(timesamps)-1):
# #for j in range(5):
    T_out = T[j, 0]
    #Node 0
    T[j+1,0] = T[j,0] + fou* (T[j,1] - T[j,0] + heatfac * Q_dot- heatfac*h*A*(T_out - T_out_amb))
    #T[0, j+1] = 27 # if fixed boundary condition
    #  (last Node)
    T_in = T[j,len(x)-1] # 5 nodes then 0,1,2,3,4,5,len(x)=6, - 1
    T[j+1,len(x)-1] = T_in + fou * (T[j,len(x)-1] - T_in) - fou*heatfac*h*A*(T_in - T_room)
    #T[len(x)-1, j+1] = 12 # if fixed boundary condition
    #interior elements 
    for i in range(1,len(x)-1):
        #print(i)
        T[j+1,i] = T[j,i] + fou * (T[j,i-1] - 2*T[j,i] + T[j,i+1])
    #print ("Intermidiate T\n",T)   


p = np.around(T, decimals=1)
print ("Final T\n",p)


# Plot 

i=0
for temperature in T:        
    plt.plot(temperature,label="{} x {} sec".format(i,dt))
    i=i+1
    plt.legend()

#ply.xlim(0.0, L)
#pyplot.ylim(0.0, 100.0);
plt.xlabel('Node')
plt.ylabel('Temperature [C]')
plt.grid()
plt.show()

