from math import sqrt

n = int(input())
ns = list(map(int, input().split()))

upper = min(ns)

for i in range(1, upper+1):
  judge = True
  for j in ns:
    if j % i != 0:
      judge = False
      break
  if judge == True:
    print(i)