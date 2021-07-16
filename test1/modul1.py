import modul2


class mathematics:
    def __init__(self):
        pass

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b


def square(x):
    return x ** 2


if __name__ == '__main__':
    math = mathematics()
    print(math.plus(2, 3))
    print(math.minus(2, 3))
    print(math.multiplication(2, 3))
    print(modul2.up('ttttteeglepo'))
    print()
    x = 2
    result = square(x)
    x = 3
    result2 = square(x)
    print(result)
    print(result2)

    print()
    x = 2
    result = lambda: x ** 2
    x = 3
    result2 = lambda: x ** 2
    print(result())
    print(result2())

    print()
    x = 2
    result = lambda x: x ** 2
    x = 3
    result2 = lambda x: x** 2
    print(result(x))
    print(result2(x))


    print()
    ints=list(range(10))
    print(list(map(lambda y:y**2, filter(lambda x:x%2==0, ints))))
    print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints))))










