money = 100000
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

for i in per_cent.values():
    deposit.append(int(i* money/100))

print(deposit)
print (max(deposit))