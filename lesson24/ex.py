try:
    file = open("myfile.txt", "a+", encoding="utf-8")
    print(file.read(2))
    file.seek(0)
    print(file.read(2))
    pos = file.tell()
    print(pos)
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readlines())
    file.writelines(["Hello\n", "Hello\n"])
    file.close()
except FileNotFoundError:
    print("Невозможно нгайти файл")
finally:
    print(file.closed)