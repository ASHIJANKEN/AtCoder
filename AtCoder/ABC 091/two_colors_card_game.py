N = int(input())

words = []

blue_cards = {}
for i in range(N):
  s = input()
  if s in blue_cards:
    blue_cards[s] = blue_cards[s] + 1
  else:
    blue_cards[s] = 1
  if s not in words:
    words.append(s)

M = int(input())

red_cards= {}
for i in range(M):
  s = input()
  if s in red_cards:
    red_cards[s] = red_cards[s] + 1
  else:
    red_cards[s] = 1
  if s not in words:
    words.append(s)

max_money = 0
for word in words:
  get_money, lose_money = 0, 0
  if word in blue_cards:
    get_money = blue_cards[word]
  if word in red_cards:
    lose_money = red_cards[word]
  max_money = max(max_money, get_money - lose_money)

print(max_money)
