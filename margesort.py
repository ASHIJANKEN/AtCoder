import time
import random
def margesort(x):
	if len(x) == 1:
		return x

	left = margesort(x[:len(x)//2])
	right = margesort(x[len(x)//2:])
	array = []

	while len(left) != 0 and len(right) != 0:
		if left[0] < right[0]:
			array.append(left.pop(0))
		else:
			array.append(right.pop(0))

	if len(left) != 0:
		array += left
	else:
		array += right

	return array

x = [random.randrange(10000) for i in range(1000)]
start = time.time()
print(margesort(x))
print ("elapsed_time:{0}".format(time.time() - start) + "[sec]")
