n = int(input())

def fact(n):
	if n == 0:
		return 1
	return n * fact(n - 1)

score_sum = 0

# 効率のいい方法を計算
a = n/2
if n%2 == 1:
	score_sum += n * fact(a)
else:
	score_sum += fact(a)

while