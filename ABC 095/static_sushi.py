n, c = [int(i) for i in input().split(" ")]

sushis_position = []
sushis_cal = []
sushis = {}
cal = 0
position = 0

for i in range(n):
	x, v = [int(i) for i in input().split(" ")]
	sushis[x] = v
	sushis_position.append(x)
	sushis_cal.append(v)

for (sp, sc) in zip(sushis_position, sushis_cal):
	distance = min([sp - position, c - sp + position])
	# print("{} {}".format(position, sp))

	if sc > distance:
		position = sp
		cal = cal + sc - distance
		# print(cal)
	else:
		# print("skip")
	# print("----------------")

print(cal)