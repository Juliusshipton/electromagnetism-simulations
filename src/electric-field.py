'''
To run make sure you pip install all the imports then run ...
    python electric-field.py
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

params = {
   'axes.labelsize': 20,
   'font.size': 20,
   'figure.figsize': [10, 10]
   } 
plt.rcParams.update(params)

def E(x,y):
    q= 1 #Charge in coulombs
    r1 = np.array([0,0]) #Charge set at origin
    e0= 8.85*10**(-12) #permetivity of free space
    mag= (q / (4 * np.pi* e0)) * (1 / ((x - r1[0])**2+ (y - r1[1])**2)) #Magnitude of Electric Field Strength
    ex= mag * ( np.sin(np.arctan2(x,y)))
    ey= mag * ( np.cos(np.arctan2(x,y)))
    
    return (ex,ey)

x=np.linspace (-10,10,14)
y=np.linspace (-10,10,14)

x,y=np.meshgrid(x,y)

ex,ey=E(x,y)
plt.quiver(x,y,ex,ey, scale = 15000000000, color="red")
plt.show()