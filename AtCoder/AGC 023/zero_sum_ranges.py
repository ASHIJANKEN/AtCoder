from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

zero_list = []

arr = list(permutations(range(n+1),2))
for l in arr:
	if l[0] >= l[1]:
		continue
	if a[l[0]:l[1]] != [] and sum(a[l[0]:l[1]]) == 0:
		if [l[0], l[1]] not in zero_list:
			zero_list.append([l[0],l[1]])

print(len(zero_list))