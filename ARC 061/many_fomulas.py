nums = list(map(int, list(input())))

def dfs(i, pluses):
  if i == len(pluses) - 1:
    pluses[i] = 0
    sum1 = calc(pluses)
    pluses[i] = 1
    sum2 = calc(pluses)
    return sum1 + sum2
  else:
    i += 1
    pluses[i] = 0
    sum1 = dfs(i, pluses)
    pluses[i] = 1
    sum2 = dfs(i, pluses)
    return sum1 + sum2

def calc(pluses):
  num = 0
  sum = 0
  for i, elm in enumerate(nums):
    num += elm
    if i == len(nums) - 1:
      sum += num
    elif pluses[i] == 1:
      sum += num
    else:
      num *= 10
  print(sum)
  return sum

print(dfs(0, [0]*(len(nums) - 1)))
