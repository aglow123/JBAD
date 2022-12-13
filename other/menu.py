def timetable():
    print('weź się do roboty')


def grades():
    print('jestes super koks')


def menu(options, functions, special_option=None, special_handler=None):      #przyjmujemy dwie listy
    for index, option in enumerate(options, start=1):
        print("{}.\t{}".format(index, option))
    valid_choices = range(1, len(options) + 1)
    while True:
        try:
            choice = int(input('What do you want to do?\n'))
            assert choice in valid_choices
            func, args, kwargs = functions[choice - 1]
            return func(*args, **kwargs)
        except (ValueError, AssertionError):
            pass


menu(['Show timetable', 'Show grades', 'Exit'], [(timetable, (), {}), (grades, (), {}), (exit, (1,), {})])
