import random

_users = [
    ("Ivan","Ivanov","test2@mail.ru", "test123"),
    ("Petr","Rubcov","test3@mail.ru", "test321"),
    ("Nik","Polyrn""test4@mail.ru", "test555")
]


def get_user():
    return random.choice(_users)
