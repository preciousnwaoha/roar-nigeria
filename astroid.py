"""This is the code to build the Astroid Curve"""
import random
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-6*np.pi, 6*np.pi, 1000) # 1000 steps between the first number and the second number - boundaries

"""So now we begin by creating a figure that contains a 3 x 3 geometry of subplots"""
fig,ax = plt.subplots(3,3)  ###<--------                            
row, col = np.indices((3,3)) 

# print(row)
# print(col)
# print(row.ravel()[3])
# print(col.ravel()[6])
for i in range(9): # n = {0, 1, 2, 3, 4, 5,}
    a = t**i # what should be the boundary of t?

    x = a * np.cos(t)**4
    y = a * np.sin(t)**4

    r = row.ravel()[i]
    c = col.ravel()[i]
    color = f"#{str(random.randint(100000, 999999))}" # random dark color generator
    ax[r,c].plot(x,y, color)
    ax[r,c].axis("on")
    ax[r,c].axis("square")

plt.show()