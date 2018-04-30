s = int(input())

otsuri = 1000 - s

coins = [500, 100, 50, 10, 5, 1]
coin_num = 0

for i in coins:
  if otsuri < i:
    continue

  c = otsuri // i
  coin_num += c
  otsuri -= i * c

print(coin_num)