#! Just a simple program
import calculation as calc
from colorama import Fore, Back, Style, Cursor, init
from termcolor import colored
init(autoreset=True, convert=True)
print(Fore.MAGENTA + "Прога считает суточную норму потребления калорий.\n")
print(colored('Результат верен только для людей обычного телосложения.', 'red', 'on_blue', attrs=['bold']))
while True:
    gender = str(input("Какой пол: М или Ж: "))
    if gender == 'ж':
        print(Style.BRIGHT + 'Пол выбран: ', gender)
        try:
         weight = float(input("Ваш Вес: "))
         height = float(input("Ваш рост: "))
         age = float(input("Ваш возраст: "))
         indexresult = calc.female(weight, height, age)
         activity = float(input("Ваша активность:(Минимум=1, низкая=2, средняя=3, высокая=4, очень высокая=5) "))
         norma = calc.activity(activity, indexresult)
         print(Back.GREEN + "Ваша суточная норма калорий: ", norma)
        except ValueError:
         print(Back.RED + "\aНеверные данные, попробуйте снова")
    elif gender == 'м':
        print(Style.BRIGHT+'Пол выбран: ', gender)
        try:
         weight = float(input("Ваш вес: "))
         height = float(input("Ваш рост: "))
         age = float(input("Ваш возраст: "))
         indexresult = calc.male(weight, height, age)
         activity = float(input("Ваша активность:(Минимум=1, низкая=2, средняя=3, высокая=4, очень высокая=5)"))
         norma = calc.activity(activity, indexresult)
         print(Back.GREEN + "Ваша суточная норма калорий: ", norma)
        except ValueError:
         print(Back.RED + "\aНеверные данные, попробуйте с начала")
    else:
        print(Back.RED + "\aНеверные данные, попробуйте с начала")