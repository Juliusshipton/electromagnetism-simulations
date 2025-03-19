'''
This shabang is the path to where python is installed on your computer

the output of the command 

    which python 


'''

#!/Users/juliusshipton/Repos/electromagnetism-simulations/venv/bin/python
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# Define a grid of points
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Define an electric field from a point charge at the origin
q = 1  # Charge magnitude
k = 8.99e9  # Coulomb's constant

Ex = k * q * X / (X**2 + Y**2)**(3/2)
Ey = k * q * Y / (X**2 + Y**2)**(3/2)

# Plot the electric field
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Ex, Ey, color='blue', scale=1e10)
plt.title("Electric Field of a Point Charge")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()
