#MODULE and Errors

#Повторение 
# name = input("Name: ")
# with open ("pract.py", "w") as f:
#     f.write(f'names = "{name}"\n')
# print(name)


# import sys # работает с системой 
# print(sys.builtin_module_names)
# 

# import - импортирует все 
# import core.pract
# x = core.pract.b
# y = core.pract.age
# print(x, y)


# from core import pract as f #  ипортирует чтот определенное 
# print(f"Имя: {f.names}, возрост: {f.age}")


# from tkinter import * #импортирует все 
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


# import random 
# import datetime
# import time 
# import os 
# import sys 
# import calendar
#  Самые поулярные 

# import random
#  # функция рандом, генерирует значения 
# a = random.randint(0, 100)
# b = random.random()
# list1 = [1, 3, 3 , 4, 5, 5]
# list2 = random.choice(list1)#выбирает число из list1
# print(a, b, list2) 

# import datetime
# a = datetime.datetime.today()
# print(a.strftime("%y-%m-%d "))# выводит данные год, месяц Б день и т.д.
# b = datetime.datetime.now().time().strftime("%h %m ")
# print(b)


# import os # работает как терминал 
# os.system("clear") # очищает терминал
# os.system("ls")# где наход
# print(os.getcwd())# полный путь до файла 

# import sys
# print(sys.builtin_module_names)#  показ какие системы есть в ноуте


# import calendar
# # print(calendar.month(2202, 12))
# # print(calendar.calendar(2202))
# # print(calendar.weekday(2022, 12, 9))
# print(calendar.isleap(2000))


# import time
# # print("Hellow")
# # print(time.sleep(8))#таймер, показ нижнии принт после определен времени
# # print("Nooo")

# print(time.ctime())


#try and except
# try:
#     zero = 10/0
# except ArithmeticError:
#     print("Число на ноль делить нельзя")


# try:
#     print(ad)
# except:
#     print("Error")


# try:
#     print("hellow")
# except:
#     print("print Error")
# else:
#     print("Hi")


# try:
#     num = int(input("Number: "))
#     print(num)
# except:
#     print("Change")
# print("Good game")


# #1 - Напишите программу которая будет принимать аргументы sys.argv и выводить на экран оттуда всё что передал пользователь.
import sys
print(sys.argv)


# #2 - Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте какое из 2-х значений занимает больше памяти.
import sys
a = input("Enter: ")
b = input("Enter: ")
if sys.getsizeof(a) > sys.getsizeof(b):
    print(sys.getsizeof(a))
else:
    print(sys.getsizeof(b))
    print("Ok")


# #3 Создайте программу которая спрашивает у пользователя число N для генерации пароля а затем генерирует ему пароль длиною N символов.

import random
a = (input("Number: "))
for number in a:
    b = random.choice(a)
    print(f'{b}', end=" ")

#4 -Создайте игру Камень-Ножницы-Бумага с Компьютером. Где компьютер даёт вам выбрать опцию, а сам затем генерирует своё значение. По итогу говорит выиграли вы, проиграли или ничья.
while True:
    game = int(input("""
    \U0001f387 Добро пожаловать в игру Камень-Ножницы-Бумага, вы будите играть против компьютера.
    \U0001f531Выберите вариант:
    1 - Камень
    2 - Ножницы
    3 - Бумага
    4 - Выити из игры
    """))
    g = [1,2,3]
    if game == 1:
        import random
        b = random.choice(g)
        if b ==1:
            print("Ничья\U0001f4f5")
        elif b ==2:
            print("Вы выиграли\U0001f3c5")
        elif b ==3:
            print("Победил компьютер\U0001f387")

    elif game ==2:
        import random
        c = random.choice(g)
        if c ==2:
            print("Ничья\U0001f4f5")
        elif c ==3:
            print("Вы выиграли\U0001f3c5")
        elif c ==1:
            print("Победил компьютер\U0001f387")

    elif game ==3:
        import random
        h = random.choice(g)
        if h ==3:
            print("Ничья\U0001f4f5")
        elif h ==1:
            print("Вы выиграли\U0001f3c5")
        elif h ==2:
            print("Победил компьютер\U0001f387")

    elif game ==4:
        break