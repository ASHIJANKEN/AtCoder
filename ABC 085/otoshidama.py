n, total = map(int, input().split())

x=0
y=0
z=0

found = False
for i in range(int(total / 10000 + 1)):
  x = i
  for j in range(int((total - 10000 * i) / 5000 + 1)):
    y = j
    z = n - x - y
    sum = 10000 * x + 5000 * y + 1000 * z
    if sum == total:
      found = True
      break

  if found == True:
    break

if found == False:
  x = -1
  y = -1
  z = -1

print("{} {} {}".format(x, y, z))
