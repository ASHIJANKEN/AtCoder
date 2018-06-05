import time
import random

def quicksort(x):
  if x == []:
    return []

  small = quicksort([i for i in x[1:] if i < x[0]])
  big = quicksort([i for i in x[1:] if i >= x[0]])

  return small + [x[0]] + big


x = [i for i in range(1000)]
start = time.time()
print(quicksort(x))
print ("elapsed_time:{0}".format(time.time() - start) + "[sec]")
