import heapq

N, K = map(int, input().split())

machines = []
for i in range(N):
  machines.append(list(map(int, input().split())))
  machines[i] = machines[i] + [0]

heapq.heapify(machines)

total_time = 0
for i in range(K):
  m = heapq.heappop(machines)
  total_time += m[0]
  m[2] += 1
  m[0] += m[1]
  heapq.heappush(machines, m)

print(total_time)
