import pickle

books = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190),
]

try:
    file = open("out.bin", "wb")

    try:
        pickle.dump(books, file)
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")

try:
    file = open("out.bin", "rb")

    try:
        bs = pickle.load(file)
        print(bs)
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
