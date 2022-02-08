import random
import numpy as np
import matplotlib.pyplot as plt
from pygame import Color

t = np.linspace(0, 8*np.pi, 1000)
fig, ax = plt.subplots(3,3)
row, col = np.indices((3,3))

for i in range(0, 9):
    k = i/2
    x = np.cos(k*t) * np.cos(t)
    y = np.cos(k*t) * np.sin(t)

    r = row.ravel()[i]
    c = col.ravel()[i]

    color = f"#{str(random.randint(0, 999999))}" # random dark color generator
    ax[r,c].plot(x, y, color )
    ax[r,c].axis("on")
    ax[r,c].axis("square")
plt.show()