N, K, L = map(int, input().split())
roads = []
for i in range(K):
  roads.append(list(map(int, input().split())))
trains = []
for i in range(L):
  trains.append(list(map(int, input().split())))

parents_road = [i for i in range(N+1)]
rank_road = [0 for i in range(N+1)]
parents_train = [i for i in range(N+1)]
rank_train = [0 for i in range(N+1)]

def find(parents,v):
  if parents[v] == v:
    return v
  else:
    return find(parents, parents[v])

def unite(parents, rank, v1, v2):
  v1 = find(parents, v1)
  v2 = find(parents, v2)

  if v1 == v2:
    return
  elif rank[v1] < rank[v2]:
    parents[v1] = v2
  else:
    parents[v2] = v1
    if rank[v1] == rank[v2]:
      rank[v1] += 1

def is_connected(parents, v1, v2):
  v1 = find(parents, v1)
  v2 = find(parents, v2)

  if v1 == v2:
    return True
  else:
    return False

for road in roads:
  unite(parents_road, rank_road, road[0], road[1])
for train in trains:
  unite(parents_train, rank_train, train[0], train[1])

for i in range(N):
  count = 1

  for j in range(N):
    if is_connected(parents_road, i, j) == True and is_connected(parents_train, i, j) == True:
      count += 1

  if i != N-1:
    print("{} ".format(count), end="")
  else:
    print(count)