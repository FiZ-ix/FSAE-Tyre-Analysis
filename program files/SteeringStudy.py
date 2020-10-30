import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#_______________________________________________________________________________________________________________________

run_input = input("Enter the run number you want to study: ") # example of input B1965run2
data = pd.read_excel (r'C:\Users\Fizics\Desktop\TTC\data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

#print(data.head())
#print(data.tail())

df = df.drop(df.index[0:5000])

pressure=df["P"] # kPa
camber=df["IA"] # deg
slipAngle = df["SA"] # deg
lateralForce = df["FY"] # N
verticalLoad = df["FZ"] * -1  # N
alignTorque = df["MZ"] # Nm

slipAngle = np.array(slipAngle)
verticalLoad = np.array(verticalLoad)
lateralForce = np.array(lateralForce)
camber = np.array(camber)
pressure = np.array(pressure)
alignTorque = np.array(alignTorque)

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

fig1 = plt.figure()

ax1 = fig1.add_subplot(111)

ax1.plot(slipAngle[Z1],alignTorque[Z1], c='midnightblue', label=labelAvgZ1)
ax1.plot(slipAngle[Z2],alignTorque[Z2], c='mediumblue', label=labelAvgZ2)
ax1.plot(slipAngle[Z3],alignTorque[Z3], c='slateblue', label=labelAvgZ3)
ax1.plot(slipAngle[Z4],alignTorque[Z4], c='mediumpurple', label=labelAvgZ4)
ax1.plot(slipAngle[Z5],alignTorque[Z5], c='plum', label=labelAvgZ5)
ax1.set_title('SA vs Mz')
ax1.set_xlabel('SA (deg)')
ax1.set_ylabel('Mz (Nm)')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()



plt.show()

