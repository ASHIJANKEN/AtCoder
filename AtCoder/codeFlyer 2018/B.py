A, B, N = map(int, input().split())
X = list(input())

for i in X:
	if i == 'S':
		A = max(A - 1, 0)
	elif i == 'C':
		B = max(B - 1, 0)
	elif i == 'E':
		if B > A:
			B -= 1
		elif A == 0 and B == 0:
			pass
		else:
			A -= 1

print(A)
print(B)