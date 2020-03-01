import calculation as calc
from colorama import Fore, Back, Style, Cursor, init

minimal = float(1.2)
low = float(1.375)
average = float(1.55)
high = float(1.725)
veryhigh = float(1.9)


def male(weight, height, age):
    bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    bmr = round(bmr)
    return bmr


def female(weight, height, age):
    bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    bmr = round(bmr)
    return bmr


def activity(act, bmr):
    result = 0
    if act == 1:
        result = minimal*bmr
    elif act == 2:
        result = low * bmr
    elif act == 3:
        result = average*bmr
    elif act == 4:
        result = high * bmr
    elif act == 5:
        result = veryhigh * bmr
    else:
        print(Back.RED + "\aНеверные данные, попробуйте с начала")
    return result
