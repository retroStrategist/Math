import numpy as np
import matplotlib.pyplot as plt
import random

# Calculates Ax and returns the new x and y values
def f1(x, y):
    newX = (.5 * (x  + y))
    newY = (.5* (y - x))
    return newX, newY
    
# Calculates Bx - [.5 .5] (Vertically) and returns the new x and y values
def f2(x, y):
    newX = (.5* (x - y) - .5)
    newY = (.5 *(x + y) - .5)
    return newX, newY

x = []
y = []

startX = random.randint(10, 90)
startY = random.randint(10, 90)

x.append(startX)
y.append(startY)

for i in range(50000): # Loop 50000 times
    choice = random.randint(0,1) # Coin Flip
    if choice % 2 == 0:
        newX, newY = f1(x[-1], y[-1]) # Calculate
        x.append(newX) # Append new values
        y.append(newY)
    else:
        newX, newY = f2(x[-1], y[-1]) # Calculate
        x.append(newX) # Append new values
        y.append(newY)

plt.figure(figsize=(12, 12))
plt.scatter(x, y, s = 0.01) # Create scatter plot
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()