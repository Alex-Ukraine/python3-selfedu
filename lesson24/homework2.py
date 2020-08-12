"""
Пусть имеется словарь:
Необходимо каждый элемент этого словаря сохранить в бинарном файле как объект.
Затем, прочитать этотфайл и вывести считанные объекты в консоль.
"""

import pickle

d = {"house": "дом", "car": "машина",
     "tree": "дерево", "road": "дорога",
     "river": "река"}

try:
    file = open("d.bin", "wb")

    try:
        pickle.dump(d, file)
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")

try:
    file = open("d.bin", "rb")

    try:
        bs = pickle.load(file)
        print(dict(bs))
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")