n, m = map(int,  input().split())
p = []
max_score = 0
for i in range(n):
  p.append(int(input()))

p.sort()

for i in range(4):
  low = 0
  high = n - 1
  canditate = [True for i in range(n)]

  while low <= high:
    middle = int((low + high) / 2)
    if max_score + p[middle] > m:
      canditate[middle] = False
      high = middle - 1
      # print(high)
    elif max_score + p[middle] == m:
      max_score += p[middle]
      # print(p[middle])
      break
    elif max_score + p[middle] < m:
      if p[middle] == p[-1]:
        max_score += p[-1]
        # print(p[middle])
        break
      elif canditate[middle] == True and canditate[middle+1] == False:
        max_score += p[middle]
        break
      low = middle + 1
  # print("---------")

print(max_score)