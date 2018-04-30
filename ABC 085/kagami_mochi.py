import heapq

N = int(input())

mochis = []

for i in range(N):
  mochis.append(int(input()))
heapq.heapify(mochis)

step = 0
pre_m = 1000
for i in range(N):
  m = heapq.heappop(mochis)
  if m == pre_m:
    continue
  step += 1
  pre_m = m

print(step)