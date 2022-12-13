from library.utils.admin import login, add_user, logout, search, searchby, remove_user, show_books, back
from library.utils.librarian import add_book, remove_book, return_book
from library.utils.reader import borrow_book, prolong, reserve_book


def menu(loginname, user_type, options):
    options = list(options.items())
    for num, option in enumerate(options, start=0):
        print("{}. {}".format(num, option[0]))
    correct_choices = range(0, len(options))
    while True:
        try:
            choice = int(input(">> "))
            assert choice in correct_choices
        except (ValueError, AssertionError):
            pass
        else:
            func, args, kwargs = options[choice][1]
            if choice == 0 or choice == 1:      #exit, login, logout
                return func(*args, **kwargs)
            return func(loginname, user_type, *args, **kwargs)


def show_menu(log, utype, menu_type):
    user_menu = choice_menu(menu_type, utype)
    while True:
        menu_type, log, utype = menu(log, utype, user_menu)
        user_menu = choice_menu(menu_type, utype)


def choice_menu(menu_type, utype):
    if menu_type == 'admin':
        return admin_menu
    elif menu_type == 'reader':
        return reader_menu
    elif menu_type == 'librarian':
        return librarian_menu
    elif menu_type == 'start':
        return start_menu
    elif menu_type == 'search':
        return search_menu
    elif menu_type == 'review' and utype == 'reader':
        return review_reader_menu
    elif menu_type == 'review':
        return review_menu


reader_menu = {
        "Zakończ": (exit, (1,), {}),
        "Wyloguj się": (logout, (), {}),
        "Przeglądaj": (search, (), {}),
        "Wypożycz": (borrow_book, (), {}),
        "Prolonguj": (prolong, (), {}),
        "Zarezerwuj": (reserve_book, (), {})
    }

librarian_menu = {
        "Zakończ": (exit, (1,), {}),
        "Wyloguj się": (logout, (), {}),
        "Dodaj książkę": (add_book, (), {}),
        "Usuń książkę": (remove_book, (), {}),
        "Przyjmij zwrot książki": (return_book, (), {}),
        "Dodaj czytelnika": (add_user, ('reader', ), {}),
        "Przeglądaj": (search, (), {}),
}

admin_menu = {
        "Zakończ": (exit, (1,), {}),
        "Wyloguj się": (logout, (), {}),
        "Dodaj czytelnika": (add_user, ('reader', ), {}),
        "Dodaj bibliotekarza": (add_user, ('librarian', ), {}),
        "Usuń użytkownika": (remove_user, (), {}),
        "Przeglądaj": (search, (), {}),
        "Dodaj książkę": (add_book, (), {}),
        "Usuń książkę": (remove_book, (), {}),
        "Przyjmij zwrot książki": (return_book, (), {})
}

start_menu = {
        "Wyjdź": (exit, (1,), {}),
        "Zaloguj się": (login, (), {}),
        "Zarejestruj się": (add_user, ('reader',), {})
}

search_menu = {
    "Zakończ": (exit, (1,), {}),
    "Wyloguj się": (logout, (), {}),
    "Cofnij": (back, (), {}),
    "Wyświetl wszystkie książki": (show_books, (), {}),
    "Wyszukaj po tytule": (searchby, ('title',), {}),
    "Wyszukaj po autorze": (searchby, ('author',), {}),
    "Wyszukaj po słowach kluczowych": (searchby, ('keywords',), {}),
}

review_reader_menu = {
    "Zakończ": (exit, (1,), {}),
    "Wyloguj się": (logout, (), {}),
    "Przeglądaj ponownie": (search, (), {}),
    "Wypożycz": (borrow_book, (), {}),
    "Prolonguj": (prolong, (), {}),
    "Zarezerwuj": (reserve_book, (), {})
}

review_menu = {
    "Zakończ": (exit, (1,), {}),
    "Wyloguj się": (logout, (), {}),
    "Przeglądaj ponownie": (search, (), {}),
    "Dodaj książkę": (add_book, (), {}),
    "Usuń książkę": (remove_book, (), {}),
    "Przyjmij zwrot książki": (return_book, (), {})
}

if __name__ == '__main__':
    show_menu('', '', 'start')
