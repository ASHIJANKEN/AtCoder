N, W = map(int, input().split())
#dp[何番目の品物][重さ]
dp = [[-1 for i in range(W+1)] for j in range(N+1)]

items = []
for i in range(N):
  items.append(list(map(int, input().split())))

# i:i番目の荷物 empty:残り容量
def rec(i, empty):
  if dp[i][empty] != -1:
    return dp[i][empty]

  res = 0
  if i == N:
    pass
  elif empty < items[i][1]:
    res = rec(i+1, empty)
  else:
    res = max(rec(i+1, empty), rec(i+1, empty - items[i][1]) + items[i][0])

  dp[i][empty] = res
  return res

print(rec(0, W))
