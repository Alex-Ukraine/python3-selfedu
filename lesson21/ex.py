# def sq(x):
#     return x**2
#
#
# lst = [1, -2, 3, -4, -5]
# b = map(sq, lst) # у функции только один аргумент
# a = list(b)
# print(a)

# lst = ["Киев", "Тернополь","Нью-Йорк", "Вена"]
# b = map(str.upper, lst)
# a = list(b)
# print(a)
#
# b = map(lambda x: x[::-1], lst)
# a = list(b)
# print(a)
#
# b = map(lambda x: x.replace("е", "Е"), lst)
# a = list(b)
# print(a)
#
# b = map(lambda x: x.replace("е", "Е"), lst)
# c = map(sorted, b)
# a = list(c)
# print(a)
#
# a = list(map(int, input().split()))
# print(a)


def odd(x):
    return x%2


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b = filter(odd, a)
b = filter(lambda x: not x%2, a)
print(list(b))

lst = ["Киев", "Терн1ополь","Нью-Йорк", "Вена"]
b = filter(str.isalpha, lst)
print(list(b))