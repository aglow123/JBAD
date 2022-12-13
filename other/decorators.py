def outer(f):
    def inner():
        print('f wywolane', )
        f()
        print('f zakonczone')
        pass
    return inner


def logged(f):
    def logged_inner(*args, **kwargs):
        print('funkcja ', f.__name__, ' wywolana z parametrem ', args, kwargs)
        result = f(*args, **kwargs)
        print('funkcja ', f.__name__, ' zakonczona z wynikiem ', result)
        return result
    return logged_inner


def memoize(f):
    buffer = {}     #słownik argumenty:wartosc f

    def memoize_inner(*args, **kwargs):
        try:
            return buffer[(args, tuple(kwargs.items()))]
        except KeyError:
            result = f(*args, **kwargs)
            buffer[(args, tuple(kwargs.items()))] = result
            return result

        # if (args, kwargs) not in list(buffer.keys()):
        #     buffer[(args, *kwargs)] = f(*args, **kwargs)
        #
        # print(buffer)
        # return buffer[(args, *kwargs)]

    return memoize_inner


@logged
def foo(x):
    return x**2
    # print('hello world')


@memoize
def fibb(n):
    if n < 3:
        return 1
    else:
        return fibb(n-2) + fibb(n-1)


# print(foo(2))
print(fibb(11))
