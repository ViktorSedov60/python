per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # Данные
max_key = max(per_cent, key=lambda k: per_cent[k]) # Вытаскиваем лучший банк
many = int(input('сколько бабок вложить?:')) # запрос на лишние бабки
# создаем цикл на результат через год
for key in per_cent:
    per_cent[key] = int(per_cent[key] * many / 100)
deposit = (list(per_cent.values()))
# Сколько получилось?
print(deposit)
# ищем максимальную сумму
max = max(deposit)
print(max)