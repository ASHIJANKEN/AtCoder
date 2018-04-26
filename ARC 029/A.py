n = int(input())
t = []

for i in range(n):
  t.append(int(input()))

minimum = 1000
diff = 1000
for i in range(1 << n):
  a, b = [], []
  for j in reversed(t):
    if i&1 == 1:
      a.append(j)
    else:
      b.append(j)
    i = i >> 1

  if abs(sum(a) - sum(b)) < diff:
    diff = abs(sum(a) - sum(b))
    minimum = max(sum(a), sum(b))

print(minimum)
