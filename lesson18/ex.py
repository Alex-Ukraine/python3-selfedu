a = 5


def myFunc(b):
    # a = 5 ERROR
    global a
    a = 10
    for x in range(b):
        n=x+1
        print(n, end=" ")
    print(x)

myFunc(6)
print("\n\n%d"%(a))

y = 0
def outer():
    # nonlocal x ERROR
    x = 1
    def inner():
        nonlocal x # использовать х уровнем выше
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)