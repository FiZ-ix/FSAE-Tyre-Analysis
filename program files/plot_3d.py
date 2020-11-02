'''
A.Q. Snyder
TFR Tire Data Analysis
this code is written to analyze the TTC FSAE tire data
the code is written in a linear, easy to read format catered towards an engineering mindset
    rather than efficient software

Contact: aaron.snyder@temple.edu for help running or understanding the program

'''
#_______________________________________________________________________________________________________________________

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#run_input = input("Enter the run number you want to study: ") # example of input B1965run2
run_input = 'B1965run2'
data = pd.read_excel (r'C:\Users\Fizics\Desktop\TTC\data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

df = df.drop(df.index[0:5000])

# SI Units are being used
# This varaibles are mostly used in the splash graph. You can add whatever other variables you want to look at

speed=df["V"]  # kph
pressure=df["P"]  # kPa
inclinationAngle=df["IA"]  # deg
slipAngle = df["SA"]  # deg
verticalLoad = df["FZ"] * -1  # N
Radius_loaded=df["RL"]  # cm
lateralForce = df["FY"]  # N
alignTorque = df["MZ"]  # Nm


slipAngle = np.array(slipAngle)
verticalLoad = np.array(verticalLoad)
lateralForce = np.array(lateralForce)


Z1 = np.where(np.logical_and(verticalLoad>= 0, verticalLoad<=320))
Z2 = np.where(np.logical_and(verticalLoad>= 320, verticalLoad<=550))
Z3 = np.where(np.logical_and(verticalLoad>= 550, verticalLoad<=750))
Z4 = np.where(np.logical_and(verticalLoad>= 750, verticalLoad<=950))
Z5 = np.where(np.logical_and(verticalLoad>= 980, verticalLoad<=1200))

labelAvgZ1 = str(np.round(np.average(verticalLoad[Z1])))+(' N')
labelAvgZ2 = str(np.round(np.average(verticalLoad[Z2])))+(' N')
labelAvgZ3 = str(np.round(np.average(verticalLoad[Z3])))+(' N')
labelAvgZ4 = str(np.round(np.average(verticalLoad[Z4])))+(' N')
labelAvgZ5 = str(np.round(np.average(verticalLoad[Z5])))+(' N')

d = 10

x1 = np.flip(np.sort(slipAngle[Z1]))
y1 = np.sort(lateralForce[Z1])
curve1 = np.polyfit(x1,y1,d)
poly1 = np.poly1d(curve1)

x2 = np.flip(np.sort(slipAngle[Z2]))
y2 = np.sort(lateralForce[Z2])
curve2 = np.polyfit(x2,y2,d)
poly2 = np.poly1d(curve2)

x3 = np.flip(np.sort(slipAngle[Z3]))
y3 = np.sort(lateralForce[Z3])
curve3 = np.polyfit(x3,y3,d)
poly3 = np.poly1d(curve3)

x4 = np.flip(np.sort(slipAngle[Z4]))
y4 = np.sort(lateralForce[Z4])
curve4 = np.polyfit(x4,y4,d)
poly4 = np.poly1d(curve4)

x5 = np.flip(np.sort(slipAngle[Z5]))
y5 = np.sort(lateralForce[Z5])
curve5 = np.polyfit(x5,y5,d)
poly5 = np.poly1d(curve5)


fig1 = plt.figure(figsize = (10,7))
ax1 = plt.axes(projection="3d")

ax1.scatter3D(slipAngle[Z1],lateralForce[Z1],verticalLoad[Z1],marker = 'x',linewidths=0.08,color = 'midnightblue')
ax1.scatter3D(slipAngle[Z2],lateralForce[Z2],verticalLoad[Z2],marker = 'x',linewidths=0.08,color = 'mediumblue')
ax1.scatter3D(slipAngle[Z3],lateralForce[Z3],verticalLoad[Z3],marker = 'x',linewidths=0.08,color = 'slateblue')
ax1.scatter3D(slipAngle[Z4],lateralForce[Z4],verticalLoad[Z4],marker = 'x',linewidths=0.08,color = 'mediumpurple')
ax1.scatter3D(slipAngle[Z5],lateralForce[Z5],verticalLoad[Z5],marker = 'x',linewidths=0.08,color = 'plum')

ax1.plot(x1, poly1(x1), c='lime', label=labelAvgZ1)
ax1.plot(x2, poly2(x2), c='lime', label=labelAvgZ1)
ax1.plot(x4, poly4(x4), c='lime', label=labelAvgZ1)
ax1.plot(x5, poly5(x5), c='lime', label=labelAvgZ1)

ax1.set_xlabel('Slip Angle')
ax1.set_ylabel('Lateral Force')
ax1.set_zlabel('Vertical Load')

plt.show()
