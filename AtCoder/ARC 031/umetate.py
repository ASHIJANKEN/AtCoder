import copy
field = []
for i in range(10):
  field.append(list(input()))

def check(f):
  for r in range(10):
    for s in range(10):
      if f[r][s] == 'o':
         return False
  return True

for i in range(10):
  for j in range(10):
    field2 = copy.deepcopy(field)
    stack = []
    stack.append([i, j])
    while len(stack) > 0:
      x, y = stack.pop()
      field2[x][y] = 'x'
      if x != 0 and field2[x-1][y] == 'o':
        stack.append([x-1, y])
      if x != 9 and field2[x+1][y] == 'o':
        stack.append([x+1, y])
      if y != 0 and field2[x][y-1] == 'o':
        stack.append([x, y-1])
      if y != 9 and field2[x][y+1] == 'o':
        stack.append([x, y+1])

    if check(field2) == True:
      print('YES')
      exit()
print('NO')