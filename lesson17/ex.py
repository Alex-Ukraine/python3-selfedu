import time


def getNOD(a, b):
    """Вычисляется НОД для натуральных чисел a и b"
        по алгоритму Евклида.
        Возвращает вычисленный НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def getNOD2(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b

    return a


print(getNOD(45, 9))
print(getNOD2(45, 9))


def testNOD(func):
    # -- test #1 -------------------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print(f"test1 {func.__name__} - ok")
    else:
        print(f"#test1  {func.__name__}- fail")

    # -- test #2 -------------------------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print(f"test2 {func.__name__}  - ok")
    else:
        print(f"#test2 {func.__name__} - fail")

    # -- test #3 -------------------------------
    a = 2
    b = 100000000

    st = time.time()
    res = func(a,b)
    et = time.time()
    dt = et-st
    print(dt)
    if res == 2 and dt < 1:
        print(f"test3 {func.__name__} - ok")
    else:
        print(f"#test3 {func.__name__} - fail")


testNOD(getNOD)
testNOD(getNOD2)