D, N = map(int, input().split())

if N == 100:
	num = 100 ** D * (N + 1)
else:
	num = 100 ** D * N

print(num)