N = int(input())
a_list = list(map(int, input().split()))

#偶数のaだけ取り出す
a_even = []
for a in a_list:
	if a % 2 == 0:
		a_even.append(a)

times = 0

while len(a_even) > 0:
	a_even[0] /= 2
	times += 1

	if a_even[0] % 2 == 1:
		a_even.pop(0)

print(times)