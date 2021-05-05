# library
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# koef p, step of array, big arrray for 5 chain, array for avverage value
p = 0.504406756
step = 30
arr = []
avr = []

# generate array of chains
for b1 in range(0,150):
  r = random.random() cr = round(math.log(1-r)/math.log(1-p))
  print(r)
  arr.append(cr)
  print(cr) 
  
# calculate average array
for b3 in range(0, 30):
  d =(arr[b3]+arr[b3 + step]+arr[b3 + step * 2]+arr[b3 + step * 3]+arr[b3 + step * 4])/5
  avr.append(d)
  print(round(d)) 
  
# printing 5 arrays
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
y = arr[0:30]
plt.plot(x,y)
plt.show()

y = arr[30:60]
plt.plot(x,y)
plt.show()

y = arr[60:90]
plt.plot(x,y)
plt.show()

y = arr[90:120]
plt.plot(x,y)
plt.show()

y = arr[120:150]
plt.plot(x,y)
plt.show()

# printing average array
y = avr[0:30]
plt.plot(x,y)
plt.show()
