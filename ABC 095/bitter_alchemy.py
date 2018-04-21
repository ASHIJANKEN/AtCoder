n, x = input().split(" ")
n = int(n)
x = int(x)

m_list = []

for i in range(n):
	m_list.append(int(input()))

m_list.sort()

donuts = 0

for i in m_list:
	x -= i
	donuts += 1

while x >= m_list[0]:
	x -= m_list[0]
	donuts += 1

print(donuts)