import numpy

n = int(input())
s = []

alpha_dict = {}
for i,c in enumerate(range(ord('a'),ord('z')+1)):
    alpha_dict[chr(c)] = i + 1

for i in range(n):
	s.append([alpha_dict[i] for i in list(input())])
count = 0

for a in range(n):
	for b in range(n):
		s2 = s[b:] + s[:b]
		for c in range(n):
			s2[c] = s2[c][a:] + s2[c][:a]
		s2 = numpy.array(s2)

		if numpy.allclose(s2, s2.T):
			if a == b:
				count += 1
			else:
				count += 2

		if a == b:
			break

print(count)