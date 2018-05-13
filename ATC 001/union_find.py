N, Q = map(int, input().split())
P = []
for i in range(Q):
  P.append(list(map(int, input().split())))

parents = [i for i in range(N)]
rank = [0 for i in range(N)]

def find(v):
  if parents[v] == v:
    return v
  else:
    return find(parents[v])

def unite(v1, v2):
  v1 = find(v1)
  v2 = find(v2)

  if v1 == v2:
    return
  elif rank[v1] < rank[v2]:
    parents[v1] = v2
  else:
    parents[v2] = v1
    if rank[v1] == rank[v2]:
      rank[v1] += 1

def is_connected(v1, v2):
  v1 = find(v1)
  v2 = find(v2)

  if v1 == v2:
    return True
  else:
    return False

for p in P:
  if p[0] == 0:
    unite(p[1], p[2])
  elif p[0] == 1:
    if is_connected(p[1], p[2]) == True:
      print('Yes')
    else:
      print('No')