#_______________________________________________________________________________________________________________________

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#_______________________________________________________________________________________________________________________

'''
pseudocode - 

get spring rate in a small region of slip angle and camber
separate pressures in both of those regions

we are not given a relaxed tire radius so we will have to find it as a function of the largest and smallest deflections
in a given region of pressure. Use the max/min Fz loads inside each pressure region and divide it by the deflection
described above with respect to the element taken for loads.
'''

#_______________________________________________________________________________________________________________________

#run_input = input("Enter the run number you want to study: ") # example of input B1965run2
run_input = 'B1965run2'
data = pd.read_excel (r'C:\Users\Fizics\Desktop\TTC\data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

#print(data.head())
#print(data.tail())

#-----------------------------------------------------------------------------------------------------------------------

pressure=df["P"]  # kPa
camber=df["IA"]  # deg
slipAngle = df["SA"]  # deg
loadedRadius = df["RL"]  # Nm
verticalLoad = df["FZ"] * -1  # N

slipAngle = np.array(slipAngle)
camber = np.array(camber)
verticalLoad = np.array(verticalLoad)
pressure = np.array(pressure)
loadedRadius = np.array(loadedRadius)

Z1 = np.where(np.logical_and(verticalLoad>= 0, verticalLoad<=320))
Z2 = np.where(np.logical_and(verticalLoad>= 320, verticalLoad<=550))
Z3 = np.where(np.logical_and(verticalLoad>= 550, verticalLoad<=750))
Z4 = np.where(np.logical_and(verticalLoad>= 750, verticalLoad<=950))
Z5 = np.where(np.logical_and(verticalLoad>= 980, verticalLoad<=1200))

# 10 psi = 68.94757 kPa
# 12 psi = 82.73709 kPa
# 14 psi = 96.5266 kPa

#-----------------------------------------------------------------------------------------------------------------------

# data points in the range of 10, 12, and 14 psi
# ref plot_2d splash chart for region divisions

pressure_10psi = np.where(np.logical_and(pressure>=np.min(pressure[2000:4000]), pressure<=np.max(pressure[2000:4000])))
pressure_12psi = np.where(np.logical_and(pressure>=np.min(pressure[0:2000]), pressure<=np.max(pressure[0:2000])))
pressure_14psi = np.where(np.logical_and(pressure<=np.min(pressure[4000:6000]), pressure<=np.max(pressure[4000:6000])))

#-----------------------------------------------------------------------------------------------------------------------

# pressure regions at small slip angles
smallSA_10psi = np.where(np.logical_and(slipAngle[pressure_10psi]>=-.1, slipAngle[pressure_10psi]<=.1))
smallSA_12psi = np.where(np.logical_and(slipAngle[pressure_12psi]>=-.1, slipAngle[pressure_12psi]<=.1))
smallSA_14psi = np.where(np.logical_and(slipAngle[pressure_14psi]>=-.1, slipAngle[pressure_14psi]<=.1))

# pressure regions at small cambers
smallC_10psi = np.where(np.logical_and(camber[pressure_10psi]>=-.5, camber[pressure_10psi]<=.5))
smallC_12psi = np.where(np.logical_and(camber[pressure_12psi]>=-.5, camber[pressure_12psi]<=.5))
smallC_14psi = np.where(np.logical_and(camber[pressure_14psi]>=-.5, camber[pressure_14psi]<=.5))

#-----------------------------------------------------------------------------------------------------------------------

# Fz loads within both small slip angles and pressure ranges

load_10psi_slipAngle = verticalLoad[smallSA_10psi]
max10psi_slipAngle = np.max(load_10psi_slipAngle)
element_max10psi_slipAngle = np.argmax(load_10psi_slipAngle)

min10psi_slipAngle = np.min(load_10psi_slipAngle)
element_min10psi_slipAngle = np.argmin(load_10psi_slipAngle)
deltaLoad10psi_slipAngle = max10psi_slipAngle - min10psi_slipAngle


load_12psi_slipAngle = verticalLoad[smallSA_12psi]
max12psi_slipAngle = np.max(load_12psi_slipAngle)
element_max12psi_slipAngle = np.argmax(load_12psi_slipAngle)

min12psi_slipAngle = np.min(load_12psi_slipAngle)
element_min12psi_slipAngle = np.argmin(load_12psi_slipAngle)
deltaLoad12psi_slipAngle = max12psi_slipAngle - min12psi_slipAngle


load_14psi_slipAngle = verticalLoad[smallSA_14psi]
max14psi_slipAngle = np.max(load_14psi_slipAngle)
element_max14psi_slipAngle = np.argmax(load_14psi_slipAngle)

min14psi_slipAngle = np.min(load_14psi_slipAngle)
element_min14psi_slipAngle = np.argmin(load_14psi_slipAngle)
deltaLoad14psi_slipAngle = max14psi_slipAngle - min14psi_slipAngle



# Fz loads within both small camber and pressure ranges
load_10psi_camber = verticalLoad[smallC_10psi]
max10psi_camber = np.max(load_10psi_camber)
#element_max10psi_camber = np.where(load_10psi_camber == np.max(load_10psi_camber)) # another method
element_max10psi_camber = np.argmax(load_10psi_camber)

min10psi_camber = np.min(load_10psi_camber)
element_min10psi_camber = np.argmin(load_10psi_camber)
deltaLoad10psi_camber = max10psi_camber - min10psi_camber


load_12psi_camber = verticalLoad[smallC_12psi]
max12psi_camber = np.max(load_12psi_camber)
element_max12psi_camber = np.argmax(load_12psi_camber)

min12psi_camber = np.min(load_12psi_camber)
element_min12psi_camber = np.argmin(load_12psi_camber)
deltaLoad12psi_camber = max12psi_camber - min12psi_camber


load_14psi_camber = verticalLoad[smallC_14psi]
max14psi_camber = np.max(load_14psi_camber)
element_max14psi_camber = np.argmax(load_14psi_camber)

min14psi_camber = np.min(load_14psi_camber)
element_min14psi_camber = np.argmin(load_14psi_camber)
deltaLoad14psi_camber = max14psi_camber - min14psi_camber

#-----------------------------------------------------------------------------------------------------------------------

# deflected tire radius at both small slip angles and pressure ranges
compressedRadius_10psi_slipAngle = loadedRadius[smallSA_10psi]
deltaDeflection10psi_slipAngle = compressedRadius_10psi_slipAngle[element_min10psi_slipAngle] - compressedRadius_10psi_slipAngle[element_max10psi_slipAngle]

compressedRadius_12psi_slipAngle = loadedRadius[smallSA_12psi]
deltaDeflection12psi_slipAngle = compressedRadius_12psi_slipAngle[element_min12psi_slipAngle] - compressedRadius_12psi_slipAngle[element_max12psi_slipAngle]

compressedRadius_14psi_slipAngle = loadedRadius[smallSA_14psi]
deltaDeflection14psi_slipAngle = compressedRadius_14psi_slipAngle[element_min14psi_slipAngle] - compressedRadius_14psi_slipAngle[element_max14psi_slipAngle]



# deflected tire radius at both small cambers and pressure ranges
compressedRadius_10psi_camber = loadedRadius[smallC_10psi]
deltaDeflection10psi_camber = compressedRadius_10psi_camber[element_min10psi_camber] - compressedRadius_10psi_camber[element_max10psi_camber]

compressedRadius_12psi_camber = loadedRadius[smallC_12psi]
deltaDeflection12psi_camber = compressedRadius_12psi_camber[element_min12psi_camber] - compressedRadius_12psi_camber[element_max12psi_camber]

compressedRadius_14psi_camber = loadedRadius[smallC_14psi]
deltaDeflection14psi_camber = compressedRadius_14psi_camber[element_min14psi_camber] - compressedRadius_14psi_camber[element_max14psi_camber]

#-----------------------------------------------------------------------------------------------------------------------

# Average Tire rates at

tireRate_10psi_slipAngle = (deltaLoad10psi_slipAngle / deltaDeflection10psi_slipAngle)
tireRate_12psi_slipAngle = (deltaLoad12psi_slipAngle / deltaDeflection12psi_slipAngle)
tireRate_14psi_slipAngle = (deltaLoad14psi_slipAngle / deltaDeflection14psi_slipAngle)


tireRate_10psi_camber = (deltaLoad10psi_camber / deltaDeflection10psi_camber)
tireRate_12psi_camber = (deltaLoad12psi_camber / deltaDeflection12psi_camber)
tireRate_14psi_camber = (deltaLoad14psi_camber / deltaDeflection14psi_camber)


print(str(tireRate_10psi_slipAngle * 0.5710147) + ' lb/in at 10psi, and small slip angle')
print(str(tireRate_12psi_slipAngle * 0.5710147) + ' lb/in at 12psi, and small slip angle')
print(str(tireRate_14psi_slipAngle * 0.5710147) + ' lb/in at 14psi, and small slip angle\n')

print(str(tireRate_10psi_camber * 0.5710147) + ' lb/in at 10psi, and small camber')
print(str(tireRate_12psi_camber * 0.5710147) + ' lb/in at 12psi, and small camber')
print(str(tireRate_14psi_camber * 0.5710147) + ' lb/in at 14psi, and small camber\n')

#  N to lb = 0.22480894244319
#  cm to in = 0.3937008
#  N/cm to lb/in = 0.5710147

#-----------------------------------------------------------------------------------------------------------------------

# in the future it will be useful to map these to a function of heat as well

# it is also important to realize that speed is a function of the tire rate as well. Spring rate increases with speed,
# since centrifugal force is spreading the tire out (one of the reasons that the tire radius in the data is larger
# than the rated static diameter on Hoosiers site.

# https://www.hoosiertire.com/contingency_rates/fsae/ ---- data from hoosier on tire rates


'''

# If you want instantaneous.....then

plt.plot(np.linspace(0,len(smallSA_10psi[0]),len(smallSA_10psi[0])),verticalLoad[smallSA_10psi])
plt.plot(np.linspace(0,len(smallSA_10psi[0]),len(smallSA_10psi[0])),loadedRadius[smallSA_10psi]*8)
# multiplying by 8 is just to show that the line is not flat....8 means nothing, stop staring at it
plt.show()

the graph above should sum up what I am trying to say. The blue line is the vertical loads in the 10 psi range of data.
The orange line is the loaded radii, both plotted against # elements in the x direction. So the tire rate is the
quotient of the two points on any given vertical line of this graph. 

However, what we are doing is taking the min and max values for load.....so basically we are finding the average
spring rate over the entire range of loads (makes sense if you look at the value in the middle of the y axis of
this graph)

Hoosier is agreeing with our data in that you can have a wide range of Fz loads but it does not affect our
pressure too much. We too have Fz loads from about 100 all the way up to 1000 N and it is still in the
10 psi range. Therefore we need to sort the data over a range of Fz's, then do the same calc we just did originally.

Then maybe we can make three plots. One for each vertical load vs deflection. Using that we can make a surface plot
where taking the gradient at any point of interest will yeild a tire rate for a given input of 
pressure and vertical load!
'''

