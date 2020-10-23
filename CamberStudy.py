'''
The TTC data should be done in either slip-angle or slip-ratio sweeps, depending on whether you're looking at the
lateral or longitudinal data. Each sweep is usually done at a different combination tire pressure, normal load or
inclination angle. So you should be able to extract Lateral Force vs Slip angle plots from 0 inclination, 2 deg
inclination, and 4 deg inclination. Viewing the difference of these plots should show the effect of Camber at that
setting of tire pressure and normal load.
'''

'''
pseudo code -

We want output graphs of Lateral Force vs Slip Angle of 0, 2, and 4 degrees of camber
Lateral Force[IA[FZ]]
Slip Angle[IA[FZ]]
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#_______________________________________________________________________________________________________________________

run_input = input("Enter the run number you want to study: ") # example of input B1965run2
data = pd.read_excel ('data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

#print(data.head())
#print(data.tail())

df = df.drop(df.index[0:5000])

pressure=df["P"] # kPa
camber=df["IA"] # deg
slipAngle = df["SA"] # deg
lateralForce = df["FY"] # N
verticalLoad = df["FZ"] * -1  # N

slipAngle = np.array(slipAngle)
verticalLoad = np.array(verticalLoad)
lateralForce = np.array(lateralForce)
camber = np.array(camber)
pressure = np.array(pressure)


# range returned is the row number, not the value
C1 = np.where(np.logical_and(camber>= 0, camber<=2))
C2 = np.where(np.logical_and(camber>= 2, camber<=3))
C3 = np.where(np.logical_and(camber>= 3, camber<=4))

labelAvgC1 = str(np.average(camber[C1]))+(' deg')
labelAvgC2 = str(np.average(camber[C2]))+(' deg')
labelAvgC3 = str(np.average(camber[C3]))+(' deg')


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

ax1.plot(slipAngle[Z1],lateralForce[Z1], c='midnightblue', label=labelAvgZ1)
ax1.plot(slipAngle[Z2],lateralForce[Z2], c='mediumblue', label=labelAvgZ2)
ax1.plot(slipAngle[Z3],lateralForce[Z3], c='slateblue', label=labelAvgZ3)
ax1.plot(slipAngle[Z4],lateralForce[Z4], c='mediumpurple', label=labelAvgZ4)
ax1.plot(slipAngle[Z5],lateralForce[Z5], c='plum', label=labelAvgZ5)
ax1.set_title('SA vs Fy')
ax1.set_xlabel('SA (deg)')
ax1.set_ylabel('Fy (N)')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()



fig2 = plt.figure()

ax2 = fig2.add_subplot(111)

ax2.plot(slipAngle[C1],lateralForce[C1], c='red', label=labelAvgC1)
ax2.plot(slipAngle[C2],lateralForce[C2], c='green', label=labelAvgC2)
ax2.plot(slipAngle[C3],lateralForce[C3], c='blue', label=labelAvgC3)
ax2.set_title('SA vs Fy')
ax2.set_xlabel('SA (deg)')
ax2.set_ylabel('Fy (N)')
plt.legend(facecolor='grey', title='@Camber=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()

fig3 = plt.figure()

ax3 = fig3.add_subplot(111)
ax3.plot(slipAngle[C1],verticalLoad[C1], c='r')
ax3.plot(slipAngle[C2],verticalLoad[C2], c='g')
ax3.plot(slipAngle[C3],verticalLoad[C3], c='b')
ax3.set_title('SA vs Fz')
ax3.set_xlabel('SA (deg)')
ax3.set_ylabel('Fz (N)')
#ax3.axhline(y=320, linewidth=3.14, c='crimson')
#ax3.axhline(y=550, linewidth=3.14, c='crimson')
#ax3.axhline(y=750, linewidth=3.14, c='crimson')
#ax3.axhline(y=980, linewidth=3.14, c='crimson')
plt.grid()


fig4 = plt.figure(figsize = (10,7))
ax4 = plt.axes(projection="3d")

ax4.scatter3D(slipAngle[C1],verticalLoad[C1],lateralForce[C1],marker = 'x',linewidths=0.08,color = 'r')
ax4.scatter3D(slipAngle[C2],verticalLoad[C2],lateralForce[C2],marker = 'x',linewidths=0.08,color = 'g')
ax4.scatter3D(slipAngle[C3],verticalLoad[C3],lateralForce[C3],marker = 'x',linewidths=0.08,color = 'b')
ax4.set_xlabel('Slip Angle')
ax4.set_ylabel('Vertical Load')
ax4.set_zlabel('Lateral Force')

plt.show()

