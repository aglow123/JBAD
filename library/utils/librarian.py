import csv
import shutil
from tempfile import NamedTemporaryFile


fieldnames_book = ['bookID', 'title', 'author', 'keywords', 'isBorrowed', 'borrowDate', 'borrowLogin', 'isReserved', 'reserveDate', 'reserveLogin']


def get_last_bookid():
    with open('books.csv', 'r', newline='') as books:
        reader = csv.DictReader(books, fieldnames=fieldnames_book)
        index = list(reader)[-1]
        return int(index.get('bookID'))


def add_book(user_login, user_type):
    index = get_last_bookid() + 1
    with open('books.csv', 'a', newline='') as books:
        writer = csv.DictWriter(books, fieldnames=fieldnames_book)
        title = input('title: ')
        author = input('author: ')
        keywords = input('keywords: ')
        writer.writerow({'bookID': index, 'title': title, 'author': author, 'keywords': keywords, 'isBorrowed': 0, 'borrowDate': None, 'borrowLogin': None, 'isReserved': 0, 'reserveDate': None, 'reserveLogin': None})
    return user_type, user_login, user_type


def remove_book(user_login, user_type):
    bookid = input('bookID: ')
    filename = 'books.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_book)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_book)
        i = 0       #to check if bookid was in the file
        for row in reader:
            if row['bookID'] != bookid:
                writer.writerow(row)
            else:
                i = 1
        if i == 0:
            print('Cannot delete - book with this bookID does not exist.')

    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type


def return_book(user_login, user_type):
    bookid = input('bookID: ')
    filename = 'books.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_book)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_book)

        for row in reader:
            if row['bookID'] == bookid:
                if row['isBorrowed'] == '1':
                    row['isBorrowed'] = 0
                    row['borrowDate'] = None
                    row['borrowLogin'] = None
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type



