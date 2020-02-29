n_num = int(input())
n_list = list(map(int, input().split()))
q_num = int(input())
q_list = list(map(int, input().split()))

count = 0
for q in q_list:
	lower = 0
	higher = len(n_list) - 1
	m = (higher - lower) // 2

	while lower <= higher:
		if n_list[m] == q:
			count += 1
			break
		elif n_list[m] > q:
			higher = m - 1
			m = lower + (higher - lower) // 2
		else:
			lower = m + 1
			m = lower + (higher - lower) // 2

print(count)