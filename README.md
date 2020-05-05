# External wall heat transfer

## Problem
The wall of a cold room is exposed to solar radiation over a period of time. The wall is made of an insulating material with thermal conductivity of 0.038 W/m-K, specific heat capacity of 700 J/kg-K and density of 120 kg/m<sup>3</sup>. The wall can be considered as infinite in two -dimensions and finite along the thickness of 15 cm. Once the wall is exposed to radiation, the temperature across the wall starts increasing from a uniform initial value of 20˚C across thickness. 

Assume an average constant radiation of 650 W/m<sup>2</sup>; outdoor and indoor air temperature maintained at 27˚C and 12˚C, respectively; average heat transfer coefficient to be 15 W/m<sup>2</sup>-K; formulate the transient heat transfer problem in terms of difference equations with appropriate boundary condition. 

![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/problem1.JPG "Node i")

```python
A = 1 # cross sectional area of wall element in m^2
rho = 120.0 # density of wall material in kg / m^3
k = 0.038 # thermal conductivity of wall material in W / (m*C)
c = 700.0 # specific heat capacity in J / (kg*C)
h = 20.0 # convective heat transfer coefficient in W / (m^2 * C)
T_initial = 23.0 # initial temperature in deg c
T_room = 12.0 # ambient temperature in deg c
T_out_amb = 27.0 # ambient temperature in deg c
L = 0.15 # thickness of the entire wall in meters
Q_dot = 650.0 # Solar Radiation in watts/sqm
N = 5 # number of discrete wall segments
total_time = 3600.0 # total duration of simulation in seconds
nsteps = 100 # number of timesteps
```


```python
dx = L/N # length of each wall segment in meters(baby step in space)
dt = total_time/nsteps # duration of timestep in seconds (baby step in time)
alpha = k/(rho*c) # Thermal diffusivity
fou =  alpha * dt /(dx*dx)         #(k*dt) / (c*rho*dx*dx) Fourier number 
heatfac = dx / (k*A) # heat fraction
```

Simultaneous equations (at each node)


 alpha . d <sup>2 </sup>T/dx<sup>2</sup> = dT/dt 
 


![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/1.JPG "Node i")

![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/2.JPG "Node i")

## Internal nodes 
<<<<<<< HEAD
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/3.JPG "Node i")

=======
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/internalnodeeq.JPG "Node i")

 <br />where <br />

![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/fou.JPG "Node i")

 ![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/nodesnewnew.JPG "Node i")
 
 ## Node 0 
>>>>>>> 9d7e1548e78c70c7d20eb364ca698c440dc28b99
 
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/Node0.JPG "Node i")

## Last Node
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/LastNode.JPG "Node i")
```python
for j in range(len(timesamps)-1):
#for j in range(5):
   T_out = T[0, j]
   #Node 0
   T[0, j+1] = T[0,j] + fou* (T[1,j] - T[0,j] + heatfac * Q_dot- heatfac*h*A*(T_out - T_out_amb))
   #T[0, j+1] = 27 # if fixed boundary condition
   #  (last Node)
   T_in = T[len(x)-1, j]
   T[len(x)-1, j+1] = T_in + fou * (T[len(x)-2, j] - T_in) - fou*heatfac*h*A*(T_in - T_room))
   #T[len(x)-1, j+1] = 12 # if fixed boundary condition
   #interior elements 
   for i in range(len(x)-2):
      T[i+1,j+1] = T[i+1,j] + fou * (T[i,j] - 2*T[i+1,j] + T[i+2,j])
   print ("Intermidiate T\n",T)   

print ("Final T\n",T)  

```
## Output k =0.038 W/m-K 
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/Figure_1_k0_038.png "Node i")
## Output k = 0.38 W/m-K
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/Figure_1.png "Node i")
