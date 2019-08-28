 #-------------------------------------------------------------------------------
### Name:        verma_priyanka_09
###
### Author:      Priyanka Verma
###
### Created:     12/11/2015
### Regional climate model data from Greenland - 1/1/1958 to 8/31/2013.
### Data- averages of albedo and melt water production as numpy arrays
### Data trends plotted using matplotlib
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt



'''Data'''
albedo = np.load(r"AL2_mo.npy")
meltwater =  np.load(r"ME_mo.npy")

#Array Scaled for original values
A = albedo/float(50000)
B = meltwater/float(100)

#Save new arrays
np.save(r"al.npy", A)
np.save(r"me.npy",B)


'''Plots'''

#Plot Albedo array
alplot = np.load(r"al.npy",)
plt.title("Overlay- Albedo & Meltwater")
plt.colormaps = ('cool')
plt.subplot(2, 2, 1)
plt.xticks([]), plt.yticks([])

plt.imshow(A[:,:,0],origin='lower',cmap=plt.cm.hot)

meplot = np.load(r"me.npy")
plt.title("Overlay- Albedo & Meltwater")

plt.subplot(2, 2, 1)
plt.imshow(meplot[:,:,0],origin='lower',alpha = 0.7,cmap=plt.cm.hot)

#Mean of each row
X = A.mean(axis=1)
Y = B.mean(axis=1)


plt.subplot(2,2,4)
plt.title("Mean Albedo")
plt.plot(X)

plt.subplot(2,2,3)
plt.title("Mean Meltwater")
plt.plot(Y)

#calculate corr coeff
cc = np.corrcoef(X,Y)
plt.subplot(2,2,2)
plt.title("Correlation Coefficient")
plt.imshow(cc)

plt.show()
