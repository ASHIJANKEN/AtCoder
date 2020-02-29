from heapq import heapify, heappop, heappush
N, M = map(int, input().split())

cakes = []
kirei = []
kirei_neg = []
oisii = []
oisii_neg = []
ninki = []
ninki_neg = []

for i in range(N):
    cake = list(map(int, input().split()))
    kirei.append([-cake[0], i])
    kirei_neg.append([cake[0], i])
    oisii.append([cake[1], i])
    oisii_neg.append([cake[1], i])
    ninki.append([cake[2], i])
    ninki_neg.append([cake[2], i])

#まずは綺麗さで最大を求める
heapify(kirei)
heapify(kirei_neg)

kirei_total = 0
kirei_neg_total = 0
kirei_list = []
kirei_neg_list = []
for i in range(M):
    a = heappop(kirei)[0]
    kirei_total += a[0]
    kirei_list.append(a[1])
    b = heappop(kirei_neg)[0]
    kirei_neg_total += b[0]
    kirei_neg_list.append(b[1])

if kirei_total < kirei_neg_total:
    kirei_list = kirei_neg_list

#次においしさで最大を求める
heapify(oisii)
heapify(oisii_neg)

oisii_total = 0
oisii_neg_total = 0
oisii_list = []
oisii_neg_list = []
for i in range(M):
    a = heappop(oisii)[0]
    oisii_total += a[0]
    oisii_list.append(a[1])
    b = heappop(oisii_neg)[0]
    oisii_neg_total += b[0]
    oisii_neg_list.append(b[1])

if oisii_total < oisii_neg_total:
    oisii_list = oisii_neg_list

#最後に人気で最大を求める
heapify(ninki)
heapify(ninki_neg)

ninki_total = 0
ninki_neg_total = 0
ninki_list = []
ninki_neg_list = []
for i in range(M):
    a = heappop(ninki)[0]
    ninki_total += a[0]
    ninki_list.append(a[1])
    b = heappop(ninki_neg)[0]
    ninki_neg_total += b[0]
    ninki_neg_list.append(b[1])

if ninki_total < ninki_neg_total:
    ninki_list = ninki_neg_list

kirei_set = set(kirei_list)
oisii_set = set(oisii_list)
ninki_set = set(ninki_list)

common = kirei_set & oisii_set & ninki_set

not_common = kirei_list + oisii_list + ninki_list - common

