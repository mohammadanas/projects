#%matplotlib inline
import matplotlib.pyplot as plt
import math as math
from mpl_toolkits import mplot3d
import numpy as np


def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def collatz(number):

    produced_numbers = []
    number_sequence = []
    count = 0
    while number > 1 and count < 100000:
       count += 1
       produced_numbers.append(number)
       number_sequence.append(count)

       if number % 2 == 0:
          print ("Step - ", count, " Even ", int(number))
          number /= 2
       else:
          print ("Step - ", count, " Odd ", int(number))
          number *= 3
          number += 1

    if count >= 100000:
      print ("Counter breached")
    return (number_sequence, produced_numbers)

def plot(x, y):
  plt.plot(x, y)
  plt.xlabel('number_sequence')
  plt.ylabel('produced_numbers')
  plt.show()

def plot3d(x, y, z):
  fig = plt.figure()
  ax = plt.axes(projection='3d')

  ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
  ax.set_title('Surface plot')
  plt.show()


number = int(input('Enter a number: '))
result = collatz(number)

x = np.array(result[0])
y = np.array(result[1])
