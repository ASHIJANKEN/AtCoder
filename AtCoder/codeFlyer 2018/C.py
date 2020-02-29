import itertools

N, D = map(int, input().split())
X_list = list(map(int, input().split()))

canditate_range = []
for begin in range(0, N - 3):
	for end in range(begin+2, N):
		if X_list[end] - X_list[begin] > 2 * D:
			canditate_range.append([begin, end - 1])
		elif end == N - 1:
			canditate_range.append([begin, end])

canditate = []
for begin, end in canditate_range:
	for c in itertools.combinations(X_list[begin:end+1], 3):
		if c not in canditate:
			canditate.append(c)

sum = 0
for c in canditate:
	if c[1] - c[0] <= D and c[2] - c[1] <= D and c[2] - c[0] > D:
		sum += 1

print(sum)