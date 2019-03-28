from app_3t.core.data_storage import *

def occurrence ():
    print("please make authorization")
    name = input ("Input name of user ")
    password = input(f"Input password for {name}")
    try:
        user = read_from_memory(name)
    except FileNotFoundError:
        print("Invalid user name, please try again ")
        return occurrence()
    if password != user.password:
        print("Invalid name or invalid password please try again ")
        return occurrence()
    else: return name
