# External wall heat transfer

## Problem
The wall of a cold room is exposed to solar radiation over a period of time. The wall is made of an insulating material with thermal conductivity of 0.038 W/m-K, specific heat capacity of 70 J/kg-K and density of 120 kg/m<sup>3</sup>. The wall can be considered as infinite in two -dimensions and finite along the thickness of 15 cm. Once the wall is exposed to radiation, the temperature across the wall starts increasing from a uniform initial value of 20˚C across thickness. 

Assume an average constant radiation of 600 W/m<sup>2</sup>; outdoor and indoor air temperature maintained at 27˚C and 12˚C, respectively; average heat transfer coefficient to be 15 W/m<sup>2</sup>-K; formulate the transient heat transfer problem in terms of difference equations with appropriate boundary condition. 


```python
A = 1 # cross sectional area of wall element in m^2
L = 0.15  # With of the wall in meter
nx = 6  # number of locations on the wall nodes
dx = L / (nx - 1)  # distance between two consecutive locations
k = 0.30 # thermal conductivity of wall material in W / (m*C)
ro = 120 # Density of material
cp = 70 # specific heat capacity in J / (kg*C)
alpha = k/(ro*cp)  #  thermal diffusivity 
q_left = 600 # W/sqm
h = 15 # convective heat transfer coefficient in W / (m^2 * C)
```

Simultaneous equations (at each node)

```math

```
 alpha . d <sup>2 </sup>T/dx<sup>2</sup> = dT/dt 
 


![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/1.JPG "Node i")

![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/2.JPG "Node i")

## Internal nodes 
![alt text](https://github.com/aviruch/1DHeatExplicit/blob/master/3.JPG "Node i")

 
```python
for j in range(len(timesamps)-1):
#for j in range(5):
   T_out = T[0, j]   
   T[0, j+1] = T[0,j] + simfac * (T[1,j] - T[0,j] + heatfac * Q_dot_in- heatfac * h * A * (T_out - T_out_amb))
   #T[0, j+1] = 35  # if fixed boundary temperature
   T_in = T[len(x)-1, j]   
   T[len(x)-1, j+1] = T_in + simfac * (T[len(x)-2, j] - T_in - heatfac * h * A * (T_in - T_room))
   #T[len(x)-1, j+1] = 12 # if fixed boundary temperature
   
   for i in range(len(x)-2):
      T[i+1,j+1] = T[i+1,j] + simfac * (T[i,j] - 2*T[i+1,j] + T[i+2,j])
   print ("Intermidiate T\n",T)   

```

