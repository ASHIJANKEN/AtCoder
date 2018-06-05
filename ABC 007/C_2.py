R, C = map(int, input().split())
sy, sx = [int(i) - 1 for i in input().split()]
gy, gx = [int(i) - 1 for i in input().split()]

field = []
for i in range(R):
  field.append(list(input()))

queue = []

queue.append([sy, sx])
field[sy][sx] = 0
while len(queue) > 0:
  y, x = queue.pop(0)
  if y == gy and x == gx:
    print(field[gy][gx])
    break

  score = field[y][x]
  if field[y-1][x] == '.':
    field[y-1][x] = score + 1
    queue.append([y-1, x])
  if field[y+1][x] == '.':
    field[y+1][x] = score + 1
    queue.append([y+1, x])
  if field[y][x-1] == '.':
    field[y][x-1] = score + 1
    queue.append([y, x-1])
  if field[y][x+1] == '.':
    field[y][x+1] = score + 1
    queue.append([y, x+1])