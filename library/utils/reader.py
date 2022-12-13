from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile
import shutil
import csv

fieldnames_book = ['bookID', 'title', 'author', 'keywords', 'isBorrowed', 'borrowDate', 'borrowLogin', 'isReserved', 'reserveDate', 'reserveLogin']


def borrow_book(user_login, user_type):
    bookid = input('bookID: ')
    filename = 'books.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_book)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_book)

        for row in reader:
            if row['bookID'] == bookid:
                if row['isBorrowed'] == '1' and row['isReserved'] == '1':
                    print("This book is already borrowed and reserved")
                elif row['isBorrowed'] == '1':
                    print("This book is already borrowed")
                elif row['isReserved'] == '1' and row['reserveLogin'] != user_login:
                    print("This book is reserved")
                else:
                    row['isReserved'] = 0
                    row['reserveDate'] = None
                    row['reserveLogin'] = None
                    row['isBorrowed'] = 1
                    row['borrowDate'] = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
                    row['borrowLogin'] = user_login
                    print(f"You borrowed a book with bookID {bookid}")
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type


def reserve_book(user_login, user_type):
    bookid = input('bookID: ')
    filename = 'books.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_book)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_book)

        for row in reader:
            if row['bookID'] == bookid:
                if row['isReserved'] == '1' and row['reserveLogin'] != user_login:
                    print("This book is reserved")
                else:
                    row['isReserved'] = 1
                    row['reserveDate'] = (datetime.today() + timedelta(days=14)).strftime("%Y-%m-%d")
                    row['reserveLogin'] = user_login
                    print(f"You reserved a book with bookID {bookid}")
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type


def prolong(user_login, user_type):
    bookid = input('bookID: ')
    filename = 'books.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.DictReader(csvFile, fieldnames=fieldnames_book)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames_book)

        for row in reader:
            if row['bookID'] == bookid:
                if row['isBorrowed'] == '1' and row['borrowLogin'] == user_login:
                    row['borrowDate'] = (datetime.strptime(row['borrowDate'], "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
                    print(f"You prolonged a book with bookID {bookid}")
                elif row['isBorrowed'] == '1' and row['borrowLogin'] != user_login:
                    print("you cannot prolong not your book")
                else:
                    print("you had not borrowed this book")
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    return user_type, user_login, user_type
