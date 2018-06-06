H, W = map(int, input().split())
N, M = map(int, input().split())

grid = [['.' for i in range(W)] for j in range(H)]

A = []
for i in range(N):
	A.append(list(input()))

blanks = 0
# 左上のブランクを調べる
for i in range(N):
	if A[i][0] == '#':
		break

	for j in range(M):
		if A[i][j] == '#':
			blanks += j
			break

#

count = 0
for i in range(N):
	for j in range(M):
		if A[i][j] == '.':
			continue

		for k in range(0, H-N+1):
			for l in range(0, W-M+1):
				if grid[i+k][j+l] != '#':
					grid[i+k][j+l] = '#'
					count += 1

# print(grid)
# for i in range(H):
# 	for j in range(W):
# 		if grid[i][j] == '#':
# 			# print('i;{} j;{}'.format(i,j))
# 			count += 1

print(count)