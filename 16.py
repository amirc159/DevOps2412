def get_user_age():
    try:
        user_age = int(input("enter age"))
    except BaseException:
        print("blabla")
    if user_age < 0:
        raise ValueError("age can not be negative")
    