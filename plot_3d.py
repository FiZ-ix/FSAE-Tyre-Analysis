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

run_input = input("Enter the run number you want to study: ") # example of input B1965run2
data = pd.read_excel ('data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

df = df.drop(df.index[0:5000])

#SI Units are being used
#This varaibles are mostly used in the splash graph. You can add whatever other variables you want to look at
speed=df["V"] # kph
pressure=df["P"] # kPa
inclinationAngle=df["IA"] # deg
slipAngle = df["SA"] # deg
verticalLoad = df["FZ"] * -1  # N
Radius_loaded=df["RL"] # cm
lateralForce = df["FY"] # N
alignTorque = df["MZ"] # Nm


slipAngle = np.array(slipAngle)
verticalLoad = np.array(verticalLoad)
lateralForce = np.array(lateralForce)


Z1 = np.where(np.logical_and(verticalLoad>= 0, verticalLoad<=320))
Z2 = np.where(np.logical_and(verticalLoad>= 320, verticalLoad<=550))
Z3 = np.where(np.logical_and(verticalLoad>= 550, verticalLoad<=750))
Z4 = np.where(np.logical_and(verticalLoad>= 750, verticalLoad<=950))
Z5 = np.where(np.logical_and(verticalLoad>= 980, verticalLoad<=1200))


fig = plt.figure(figsize = (10,7))
ax = plt.axes(projection="3d")

ax.scatter3D(slipAngle[Z1],verticalLoad[Z2],lateralForce[Z3],marker = 'x',linewidths=0.08,color = 'red')
ax.set_xlabel('Slip Angle')
ax.set_ylabel('Vertical Load')
ax.set_zlabel('Lateral Force')

plt.show()


