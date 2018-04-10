from math import sqrt

points_num = int(input())

points = []
for i in range(points_num):
	points.append([int(s) for s in input().split(" ")])

max_length = 0
for i in range(len(points)):
	for j in range(len(points)):
		if i == j:
			continue

		distance = sqrt(pow(points[i][1] - points[j][1], 2) + pow(points[i][0] - points[j][0], 2))
		if distance > max_length:
			max_length = distance

print(max_length)