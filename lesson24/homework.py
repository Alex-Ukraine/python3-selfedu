"""Выполните считывание данных из текстового файла через символ и записи прочитанных в другой текстовый файл.
Прочитывайте так не более 100 символов."""

with open("myfile.txt", "r+") as file:
    for n in range(100):
        if n%2:
            file.seek(n)
            ch = file.read(1)
            with open("myfile1.txt", "at", encoding="utf-8") as file1:
                file1.write(ch+"\n")
