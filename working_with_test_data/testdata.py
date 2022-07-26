from csv import DictReader
import json


def format_resp_book(book):
    tru_book = {}
    tru_book["title"] = book["Title"]
    tru_book["author"] = book["Author"]
    tru_book["pages"] = book["Pages"]
    tru_book["genre"] = book["Genre"]
    return tru_book


def format_resp_user(user):
    tru_user = {}
    tru_user["name"] = user["name"]
    tru_user["gender"] = user["gender"]
    tru_user["address"] = user["address"]
    tru_user["age"] = user["age"]
    return tru_user

"""Считывание данных по пользователям из файла и сохранение в переменную"""
with open("file_data/users.json", 'r', newline='', encoding='utf-8') as users_file:
    users = json.loads(users_file.read())

"""Считывание данных по книгам из файла и сохранение в переменную"""
with open("file_data/books.csv", 'r', newline='', encoding='utf-8') as books_file:
    reader = DictReader(books_file)
    books = []
    for row in reader:
        books.append(row)

"""Форматирование данных по пользователям"""
resp_users_list = []
for user in users:
    user_format = format_resp_user(user)
    resp_users_list.append(user_format)


"""Распределение кинг по пользователям"""
user_index = 0
book_index = 0
while book_index != len(books) - 1:
    if user_index == len(resp_users_list):
        user_index = 0
    if book_index <= user_index:
        resp_users_list[user_index]["books"] = []
    user_book = format_resp_book(books[book_index])
    resp_users_list[user_index]["books"].append(user_book)
    user_index += 1
    book_index += 1

"""Запись в результирующий файл"""
with open("result.json",  'w', newline='', encoding='utf-8') as results_file:
    json.dump(resp_users_list, results_file, indent=4)
