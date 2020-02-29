N, M = map(int, input().split())

nodes = [[] for i in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)

new_edges = []
visited = [False] * (N+1)
stack = []

for start in range(N):
  stack.append([0, start, start])

while len(stack) > 0:
  i, next_node, start_node = stack.pop()
  print([i, next_node, start_node])

  if visited[next_node] == True:
    continue
  else:
    visited[next_node] = True

  if i ==3:
    if [next_node, start_node] in new_edges or [start_node, next_node] in new_edges:
      new_edges.append([start_node, next_node])
      nodes[start_node].append(next_node)
      nodes[next_node].append(start_node)
      visited[next_node] = False
      continue

  for node in nodes[next_node]:
    stack.append([i+1, node, start_node])


print(len(new_edges))
