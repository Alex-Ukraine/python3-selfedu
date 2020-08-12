"""1. Поставить в соответствие следующием английским символам русские буквы:
h - х, e - е, l - л, o - о, w - в, r - р, d - д
и преобразовать строку 'hello world!' """

eng = "helowrd"
rus = "хеловрд"
d = dict(zip(eng, rus))
origin = 'hello world!'
tr = origin
for ch in origin:
    try:
        tr = tr.replace(ch, d[ch])
    except:
        pass

print(tr)

