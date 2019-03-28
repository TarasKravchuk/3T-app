from app_3t.core.data_storage import *

def password_checker(class_user, name_user, password):
    try:
        user  = read_from_memory(name_user)
    except FileNotFoundError: print('invalid user name')
    if user.user_informaton is (class_user, name_user, password):
        return name_user
    else: return print("Incorrect password")


def password_security():
    """Проверка секъюрности пароля при создании"""
    password = input("Please input password, the password must to contain:\nnot less then 6 symbols\nminimum 1 number\n"
    "minimum 1 capital letter \nminimum 1 low letter \nand minimum 1 symbol\n")
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0

    for i in password:
        if i.isupper() is True:
            upper_case += 1
        elif i.islower() is True:
            lower_case += 1
        elif i.isdigit() is True:
            number += 1
        else:
            symbol += 1

    if len(password) < 6:
        print("This is a weak password, please try again")
        return password_security()
    elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
        return password
    else:
        print("This is a weak password, please try again")
        return password_security()
