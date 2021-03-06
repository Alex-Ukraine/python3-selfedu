"""Используя сортировку, найдите первые три наиментшие значения в списке"""

a = [1, 2, -5, 0, 5, 10]
a = sorted(a)
print(a[0], a[1], a[2])

"""Отсортируйте список так чтобы сначала шли отрицательные числа,
а затем положительные."""

digs = (-10, 0, 7, -2, 3, 6, -8)
print(sorted(digs, key=lambda x: x>0))

"""Пусть имеется словарьЖ 
Необходимо вывести телефонные номера по убыванию чисел, указанных в ключах, то есть, в порядке
+4 +5 + 7 +12"""
d = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
# print(sorted(d, key=lambda x: int(x)))
ds = sorted(d, key=lambda x: int(x))
print([d[x] for x in ds])