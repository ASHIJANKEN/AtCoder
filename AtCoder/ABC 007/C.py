r, c = map(int, input().split())

s_pos = [int(i) - 1 for i in input().split()]
g_pos = [int(i) - 1 for i in input().split()]

map = []

for i in range(r):
  map.append(list(input()))

map[s_pos[0]][s_pos[1]] = 0

queue = [s_pos]

while len(queue) > 0:
  pos = queue.pop(0)
  if pos == g_pos:
    break

  for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    if map[pos[0]+i[0]][pos[1]+i[1]] == "#":
    	pass
    elif map[pos[0]+i[0]][pos[1]+i[1]] == ".":
      map[pos[0]+i[0]][pos[1]+i[1]] =  map[pos[0]][pos[1]] + 1
      queue.append([pos[0]+i[0], pos[1]+i[1]])

print(map[g_pos[0]][g_pos[1]])
