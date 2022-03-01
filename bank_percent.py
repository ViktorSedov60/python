per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # Данные
money = int(input('Вложенная сумма?:')) 
for key in per_cent:
    per_cent[key] = int(per_cent[key] * money / 100)
deposit = (list(per_cent.values()))
print(deposit)
max = max(deposit)
var = ("Максимальная сумма, которую вы можете заработать —")
print(var, max)