def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except (ValueError, TypeError):
            print('Podaj liczbę')


def nwd(a, b):
    a = abs(a)
    b = abs(b)
    while b > 0:
        a, b = b, a % b
    return a


def nww(a, b):
    if a >= b:
        return a * b / nwd(a, b)
    else:
        return a * b / nwd(b, a)


def nwdornww():
    print('Powiedz, co chcesz zrobić?')
    print('1 - NWD')
    print('2 - NWW')
    choice = input_int("wybór = ")
    if choice == 1:
        a = input_int('a = ')
        b = input_int('b = ')
        print(nwd(a, b))
    elif choice == 2:
        a = input_int('a = ')
        b = input_int('b = ')
        print(nww(a, b))
    else:
        print('Podałeś złą wartość')


def linear(a, b, c, d):
    # return a, b parameters from ax+b linear function passing through two given points
    if a == c and b == d:
        raise ValueError('Podane punkty są takie same')
    elif a == c:
        raise ValueError('Podane punkty nie zadają funkcji liniowej')
    elif b == d:
        return 0, b
    else:
        return (b-d)/(a-c), b - ((b-d)/(a-c))*a


def quadratic(a, b, c):
    return 0
