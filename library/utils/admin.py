import getpass
import hashlib
import csv
import shutil
from tempfile import NamedTemporaryFile

from tabulate import tabulate

fieldnames_login = ['login', 'password', 'role']
fieldnames_book = ['bookID', 'title', 'author', 'keywords',
                   'isBorrowed', 'borrowDate', 'borrowLogin',
                   'isReserved', 'reserveDate', 'reserveLogin']


def is_login_available(log):
    with open('credentials.csv', 'r', newline='') as cred:
        reader = csv.DictReader(cred, fieldnames=fieldnames_login)
        for row in reader:
            if row['login'] == log:
                print("This login is not available! Please try again")
                return False
        return True


def signup(role='reader'):
    while True:
        log = input('login: ')
        if is_login_available(log) is True:
            break
    pwd = getpass.getpass("Enter password: ")
    conf_pwd = getpass.getpass("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.csv", "a", newline='') as cred:
            writer = csv.DictWriter(cred, fieldnames=fieldnames_login)
            writer.writerow({'login': log, 'password': hash1, 'role': role})
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")


def login():
    log = input("Enter login: ")
    pwd = getpass.getpass("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('credentials.csv', 'r', newline='') as cred:
        reader = csv.DictReader(cred, fieldnames=fieldnames_login)
        for row in reader:
            if log == row['login'] and auth_hash == row['password']:
                print("Logged in Successfully!")
                return row['role'], log, row['role']
        print("Login failed! \n")
        return 'start', '', ''


def logout():
    return 'start', '', ''


def searchby(user_login, user_type, column_name):
    word = (input(f'Search by {column_name}: ')).lower()
    data = []
    if user_type == 'reader':
        headers = ['bookID', 'title', 'author', 'is borrowed', 'is reserved']
    else:
        headers = fieldnames_book
    with open('books.csv', 'r', newline='') as books:
        reader = csv.DictReader(books, fieldnames=fieldnames_book)
        for row in reader:
            if word in row[column_name].lower():
                if user_type == 'reader':
                    data.append([row['bookID'], row['title'], row['author'], row['isBorrowed'], row['isReserved']])
                else:
                    data.append([row['bookID'], row['title'], row['author'], row['keywords'],
                                 row['isBorrowed'], row['borrowDate'], row['borrowLogin'],
                                 row['isReserved'], row['reserveDate'], row['reserveLogin']])
    print(tabulate(data, headers=headers))
    return user_type, user_login, user_type


def search(user_login, user_type):
    return 'search', user_login, user_type


def add_user(user_login, user_type, role):
    signup(role)
    if user_type == '':
        return 'start', user_login, user_type
    return user_type, user_login, user_type


def remove_user(user_login, user_type):
    log = input('login: ')
    filename = 'credentials.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_login)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_login)
        i = 0       #to check if login was in the file
        for row in reader:
            if row['login'] != log:
                writer.writerow(row)
            else:
                i = 1
        if i == 0:
            print('Cannot delete - user with this login does not exist.')

    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type


def show_books(user_login, user_type):
    data = []
    if user_type == 'reader':
        headers = ['bookID', 'title', 'author', 'is borrowed', 'is reserved']
    else:
        headers = fieldnames_book
    with open('books.csv', 'r', newline='') as books:
        reader = csv.DictReader(books, fieldnames=fieldnames_book)
        for row in reader:
            if user_type == 'reader':
                data.append([row['bookID'], row['title'], row['author'], row['isBorrowed'], row['isReserved']])
            else:
                data.append([row['bookID'], row['title'], row['author'], row['keywords'],
                             row['isBorrowed'], row['borrowDate'], row['borrowLogin'],
                             row['isReserved'], row['reserveDate'], row['reserveLogin']])
    print(tabulate(data, headers=headers))
    return user_type, user_login, user_type


def back(user_login, user_type):
    return user_type, user_login, user_type
