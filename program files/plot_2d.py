'''
A.Q. Snyder

TFR Tire Data Analysis
this code is written to analyze the TTC FSAE tire data
the code is written in a linear, easy to read format catered towards an engineering mindset
rather than efficient software

Contact: aaron.snyder@temple.edu for help running or understanding the program
'''

#_______________________________________________________________________________________________________________________

'''
SECTION 1

this section contains the necessary packages used to process the data. If you are using Pycharm as your IDE, go to
File --> Settings --> Project --> choose Project Interpreter then click on the (+) sign on the right hand side to add
other packages
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#_______________________________________________________________________________________________________________________

'''
SECTION 2

The original format of this code took run8 data. If you want to add other data, make sure it is added in the same file
structure. ~$PROJECT_PATH...program files\data\.....
'''

run_input = input("Enter the run number you want to study: ") # example of input B1965run2
data = pd.read_excel ('data\RunData_cornering_ASCII_SI_10in_round8 excel/'+(run_input)+(".xlsx"),skiprows=2)
df = pd.DataFrame(data)

print(data.head())
print(data.tail())


'''
first we skipped the information in the first two rows
then the 'date' variable read the 3rd rows heads
now we delete data from 0:3600 where 0 is actually the 4th row in the excel doc. We do this to get rid of
pre test noise. Comment out the the line below to see what the splash graph looks like without it
'''
df = df.drop(df.index[0:5000])

#SI Units are being used
#This varaibles are mostly used in the splash graph. You can add whatever other variables you want to look at
speed=df["V"] # kph
pressure=df["P"] # kPa
camber=df["IA"] # deg
slipAngle = df["SA"] # deg
verticalLoad = df["FZ"] * -1  # N
Radius_loaded=df["RL"] # cm
lateralForce = df["FY"] # N
alignTorque = df["MZ"] # Nm

#_______________________________________________________________________________________________________________________

'''
SECTION 3

https://fsaettc.org/viewtopic.php?f=18&t=182&p=1099&hilit=tactics+for+TTC#p1099
This section creates a splash graph similiar to whats done in the URL above

numpy.sign - returns a -1,0, or 1 correlating to a negative, zero, or possitive value (array)
numpy.diff - returns the difference of out[]= a[i+1] - a[i] (array)
numpy.nonzero - returns values of input array that are not == 0 (tuple)
'''

slipAngle = np.array(slipAngle)
verticalLoad = np.array(verticalLoad)
lateralForce = np.array(lateralForce)

sign = np.sign(slipAngle)
diff = np.diff(sign)
xCross = np.ndarray.nonzero(diff)
xvec = np.array(range(len(slipAngle)))
xCritical = xvec[xCross]
yCritical = slipAngle[xCross]

#total_sets = (len(xCritical))  # use this line to find the number of x crossings

#num_Fz_loadvalues = 6
#num_load_set = int(total_sets/6)
a=18

fig1, ax1 = plt.subplots(6, sharex=False)

ax1[0].set_title('Data of Interest vs Indices - Splash Graph')
ax1[0].plot(speed,c='r',linewidth=0.1)
ax1[0].set_ylabel('speed (kph)')
ax1[0].axvline(x=xCritical[a])
ax1[0].grid()

ax1[1].plot(pressure,c='k')
ax1[1].set_ylabel('pressure (kPa)')
ax1[1].axvline(x=xCritical[a])
ax1[1].grid()

ax1[2].plot(camber,c='k')
ax1[2].set_ylabel('IA (deg)')
ax1[2].axvline(x=xCritical[a])
ax1[2].grid()

ax1[3].plot(slipAngle,c='k')
ax1[3].scatter(xCritical,yCritical,marker='x', c='r') #overlay a scatter of (x's) to show the x axis crossings.
ax1[3].set_ylabel('SA (deg)')
ax1[3].axvline(x=xCritical[a])
ax1[3].grid()

ax1[4].plot(verticalLoad,c='k')
ax1[4].set_ylabel('FZ (N)')
ax1[4].axvline(x=xCritical[a])
ax1[4].grid()

ax1[5].plot(Radius_loaded,c='k')
ax1[5].set_ylabel('RL (cm)')
ax1[5].axvline(x=xCritical[a])
ax1[5].set_xlabel('Indices')
ax1[5].grid()

#_______________________________________________________________________________________________________________________

'''
SECTION 4

https://stackoverflow.com/questions/1735025/how-to-normalize-a-numpy-array-to-within-a-certain-range
normalize between -1 and 1
need to look up why the data is normalized when they seem to produce identical graphs
'''

slipAngle_norm = 2.*(slipAngle-np.min(slipAngle))/np.ptp(slipAngle)-1
FY_norm = 2.*(lateralForce-np.min(lateralForce))/np.ptp(lateralForce)-1


fig2 = plt.figure()


ax2 = fig2.add_subplot(211)
ax2.plot(slipAngle,lateralForce, c='gray')
ax2.set_title('SA vs Fy')
ax2.set_xlabel('SA (deg)')
ax2.set_ylabel('Fy (N)')
plt.grid()

ax3 = fig2.add_subplot(212)
ax3.plot(slipAngle_norm,FY_norm, c='silver')
ax3.set_title('SA vs Fy Normalized')
ax3.set_xlabel('SA (deg)')
ax3.set_ylabel('Fy (N)')
plt.grid()

#_______________________________________________________________________________________________________________________

'''
SECTION 5
plot the Fz splitting lines --> this is done visually. New data sets will need the parameters in section 5 & 6 adjusted

Understand that the SA,Fy, and Fz data form a 3 dimensional plot. Essentially it is the SA vs Fy plots plotted where the
3rd axis (Fz) is the depth. When plotting the SA vs Fz graph, you are taking a top view of the SA vs Fy graph. 
'''

fig3 = plt.figure()

ax4 = fig3.add_subplot(111)
ax4.plot(slipAngle,verticalLoad, c='k')
ax4.set_title('SA vs Fz')
ax4.set_xlabel('SA (deg)')
ax4.set_ylabel('Fz (N)')
ax4.axhline(y=320, linewidth=3.14, c='crimson')
ax4.axhline(y=550, linewidth=3.14, c='crimson')
ax4.axhline(y=750, linewidth=3.14, c='crimson')
ax4.axhline(y=980, linewidth=3.14, c='crimson')
plt.grid()

#_______________________________________________________________________________________________________________________
'''
SECTION 6
sectioning the Fz ranges and plotting them
'''
# range returned is the row number, not the value
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


fig4 = plt.figure()

ax5 = fig4.add_subplot(111)

ax5.plot(slipAngle[Z1],verticalLoad[Z1], c='midnightblue', label=labelAvgZ1)
ax5.plot(slipAngle[Z2],verticalLoad[Z2], c='mediumblue', label=labelAvgZ2)
ax5.plot(slipAngle[Z3],verticalLoad[Z3], c='slateblue', label=labelAvgZ3)
ax5.plot(slipAngle[Z4],verticalLoad[Z4], c='mediumpurple', label=labelAvgZ4)
ax5.plot(slipAngle[Z5],verticalLoad[Z5], c='plum', label=labelAvgZ5)
ax5.set_xlabel('SA (deg)')
ax5.set_ylabel('Fz (N)')
ax5.set_title('SA vs Fz')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()

#_______________________________________________________________________________________________________________________

'''
SECTION 7
single plot with all SA vs Fy at different Fz
'''

fig5 = plt.figure()

ax6 = fig5.add_subplot(111)

ax6.plot(slipAngle[Z1],lateralForce[Z1], c='midnightblue', label=labelAvgZ1)
ax6.plot(slipAngle[Z2],lateralForce[Z2], c='mediumblue', label=labelAvgZ2)
ax6.plot(slipAngle[Z3],lateralForce[Z3], c='slateblue', label=labelAvgZ3)
ax6.plot(slipAngle[Z4],lateralForce[Z4], c='mediumpurple', label=labelAvgZ4)
ax6.plot(slipAngle[Z5],lateralForce[Z5], c='plum', label=labelAvgZ5)
ax6.set_title('SA vs Fy')
ax6.set_xlabel('SA (deg)')
ax6.set_ylabel('Fy (N)')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()

#_______________________________________________________________________________________________________________________

'''
SECTION 8
splitting and splashing the SA vs Fy with respect to different Fz
'''

fig6 = plt.figure()

ax7 = fig6.add_subplot(511)
ax7.plot(slipAngle[Z1],lateralForce[Z1], c='midnightblue', label=labelAvgZ1)
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)

ax8 = fig6.add_subplot(512)
ax8.plot(slipAngle[Z2],lateralForce[Z2], c='mediumblue', label=labelAvgZ2)
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)

ax9 = fig6.add_subplot(513)
ax9.plot(slipAngle[Z3],lateralForce[Z3], c='slateblue', label=labelAvgZ3)
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)

ax10 = fig6.add_subplot(514)
ax10.plot(slipAngle[Z4],lateralForce[Z4], c='mediumpurple', label=labelAvgZ4)
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)

ax11 = fig6.add_subplot(515)
ax11.plot(slipAngle[Z5],lateralForce[Z5], c='plum', label=labelAvgZ5)
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
ax11.set_xlabel('SA (deg)')

#_______________________________________________________________________________________________________________________

'''
SECTION 9
poly-fitting & magic formula stuff
still not sure if using the magic formula to spline fit the data is really worth it. I think that modern fitting
techniques may be more worthwhile. I will try both and find their mean errors.
'''

#begin magic formula poop
alpha = slipAngle[Z1]  # slip angle (deg)
C = verticalLoad[Z1]/slipAngle[Z1]  # cornering stiffness (kg/deg) --> is the slope of the SA vs Fy curve at a given point
mu_y = 0.2  # lateral friction coefficient (0-dim) --> need a better number for this
Z = verticalLoad[Z1]  # verticalLoad
alpha_n = (C * np.arctan(alpha))/(mu_y/Z) # normalized slip angle

#curve fitting coefficients
Bp = 0.714
Cp = 1.40
Dp = 1.00
Ep = -0.20

phi = ((1-Ep)*alpha_n) + ((Ep/Bp)*np.arctan(Bp * alpha_n))
theta = Cp * (np.arctan(Bp * phi))

F_magic = Dp * np.sin(theta)  #magic formula


#begin poly fitting
fig7 = plt.figure()
d = 10

x1 = slipAngle[Z1]
y1 = lateralForce[Z1]
curve1 = np.polyfit(x1,y1,d)
poly1 = np.poly1d(curve1)

ax12 = fig7.add_subplot(511)
ax12.plot(x1, poly1(x1), c='midnightblue', label=labelAvgZ1)
ax12.scatter(slipAngle[Z1],lateralForce[Z1],c='black', marker='x')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)



x2 = slipAngle[Z2]
y2 = lateralForce[Z2]
curve2 = np.polyfit(x2,y2,d)
poly2 = np.poly1d(curve2)

ax13 = fig7.add_subplot(512)
ax13.plot(x2, poly2(x2), c='mediumblue', label=labelAvgZ2)
ax13.scatter(slipAngle[Z2],lateralForce[Z2],c='black', marker='x')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)



x3 = slipAngle[Z3]
y3 = lateralForce[Z3]
curve3 = np.polyfit(x3,y3,d)
poly3 = np.poly1d(curve3)

ax14 = fig7.add_subplot(513)
ax14.plot(x3, poly3(x3), c='slateblue', label=labelAvgZ3)
ax14.scatter(slipAngle[Z3],lateralForce[Z3],c='black', marker='x')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)



x4 = slipAngle[Z4]
y4 = lateralForce[Z4]
curve4 = np.polyfit(x4,y4,d)
poly4 = np.poly1d(curve4)

ax15 = fig7.add_subplot(514)
ax15.plot(x4, poly4(x4), c='mediumpurple', label=labelAvgZ4)
ax15.scatter(slipAngle[Z4],lateralForce[Z4],c='black', marker='x')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)



x5 = slipAngle[Z5]
y5 = lateralForce[Z5]
curve5 = np.polyfit(x5,y5,d)
poly5 = np.poly1d(curve5)

ax16 = fig7.add_subplot(515)
ax16.plot(x5, poly5(x5), c='plum', label=labelAvgZ5)
ax16.scatter(slipAngle[Z5],lateralForce[Z5],c='black', marker='x')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)

#throwing in a graph with the fitted lines on all Fz Loads of SA vs Fy

fig8 = plt.figure()

ax17 = fig8.add_subplot(111)
ax17.set_facecolor='darkgrey'

ax17.scatter(slipAngle[Z1],lateralForce[Z1], c='midnightblue', label=labelAvgZ1, s=.08)
ax17.plot(x1, poly1(x1), c='lime', label=labelAvgZ1)

ax17.scatter(slipAngle[Z2],lateralForce[Z2], c='mediumblue', label=labelAvgZ2, s=.08)
ax17.plot(x2, poly2(x2), c='lime', label=labelAvgZ2)

ax17.scatter(slipAngle[Z3],lateralForce[Z3], c='slateblue', label=labelAvgZ3, s=.08)
ax17.plot(x3, poly3(x3), c='lime', label=labelAvgZ3)

ax17.scatter(slipAngle[Z4],lateralForce[Z4], c='mediumpurple', label=labelAvgZ4, s=.08)
ax17.plot(x4, poly4(x4), c='lime', label=labelAvgZ4)

ax17.scatter(slipAngle[Z5],lateralForce[Z5], c='plum', label=labelAvgZ5, s=.08)
ax17.plot(x5, poly5(x5), c='lime', label=labelAvgZ5)

ax17.set_title('SA vs Fy')
ax17.set_xlabel('SA (deg)')
ax17.set_ylabel('Fy (N)')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()


#now just the fitted lines
fig9 = plt.figure()

ax19 = fig9.add_subplot(111)
ax19.scatter(x1, poly1(x1), c='midnightblue', label=labelAvgZ1, s=3)
ax19.scatter(x2, poly2(x2), c='mediumblue', label=labelAvgZ2, s=3)
ax19.scatter(x3, poly3(x3), c='slateblue', label=labelAvgZ3, s=3)
ax19.scatter(x4, poly4(x4), c='mediumpurple', label=labelAvgZ4, s=3)
ax19.scatter(x5, poly5(x5), c='plum', label=labelAvgZ5, s=3)
ax19.set_xlabel('SA (deg)')
ax19.set_ylabel('Fy (N)')
plt.legend(facecolor='grey', title='@Fz=', labelcolor='w', fontsize='small', fancybox=True)
plt.grid()

#_______________________________________________________________________________________________________________________

'''
SECTION 10
'''

#This command simply output all the plots defined in the code above
plt.show() #show all subplots

#_______________________________________________________________________________________________________________________

