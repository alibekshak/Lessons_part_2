# *args, **kwargs

# *args - list тип данных, может добавлять бесконечное число элементов
# **kwargs - dict принимает ключ и значение 

# def add(*args):
#     sum = 0 
#     for i in args:
#         sum += i
#     return sum

# print(add(1, 2, 33, 43, 55, 72))


# a = [3, 4, "fff", "fs", True]
# n = [ 1, 2, *a]
# print(n)

# from random import choice

# def main(*af):
#     list1 = ["Maick", "Jorg"]
#     return choice(list1), choice(af)
# print(main(13, 42 ))


# from random import choice

# man = input("Name: ")
# n = input("Job, enter wish list(mast include min 3 job): ")
# def testgo (*n):
#     return choice(n)

# with open("Something.txt", "w") as f:
#     f.write(f"Your name is {man}, your pothishon {n}")

# testgo(n)


# from random import choice
# def main(size_pass: int, *list1):
#     password = []
#     code = []
#     num_code = ['1','2','3','4','5','6','7','8','9','0']
#     for i in range(size_pass):
#         password.append(choice(list1))
#     for j in range(6):
#         if len(code) >= 6:
#             break
#         code.append(choice(num_code))
#     return password, code


# size_password = int(input('pass size: '))
# end_pass = main(size_password, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
# passs = ''.join(end_pass[0])
# code = ''.join(end_pass[1])
# print(passs, code)



# baza = {}
# import os 
# os.system('clear')
# import random
# def genric_password(nr_letters=4, nr_numbers=3, nr_sysmbool=6):
#     alph = 'qweertyuiopasdfghjklzxcvbnm'
#     num = '1234567890'
#     symbol = '!@#$%^&*()|?'
    
#     #  = int(input('how many letters do want?: '))
#     #  = int(input('how many numbers do want?: '))
#     #  = int(input('how many sysmbols do want?: '))
#     passwrod = []
#     for i in range(1, nr_letters + 1):
#         passwrod += random.choice(alph)
#     for i in range(1, nr_numbers + 1):
#         passwrod += random.choice(num)
#     for i in range(1, nr_sysmbool + 1):
#         passwrod += random.choice(symbol)

#     random.shuffle(passwrod)
    
#     password_string = ""
#     for i in passwrod:
#         password_string += i
#     return password_string

# # genric_password()

# def code_chek():
#     num = ['1','2','3','4','5','6','7','8','9','0']
#     code = ''
    
#     for i in range(1,7):
#         code += random.choice(num)
#     return int(code)

# # print(code_chek())

# while True:
#     table = int(input('''
#     register        1
#     autorization    2
#     >>> '''))
#     if table == 1:
#         login = input('login: ')
#         password2 = genric_password()
#         code = code_chek()
#         print(code)
#         try:
#             inpcode = int(input('code: '))
#         except ValueError:
#             print('пиши код в циврах')
#         else:
#             while inpcode != code:
#                 print('повторите ввод кода')
#                 inpcode = int(input('code: '))
#             else:
#                 print('ты зарегитрирован')
#                 baza.update({
#                     'login': login,
#                     'password': password2
#                 })
#                 print(baza)
#     elif table == 2:
#         login = input('login; ')
#         password2 = input('pass: ')
#         if login in baza.values():
#             if password2 in baza.values():
#                 print('вы авторизованы')
#             else:
#                 print('не верный пароль')
#         else:
#             print('у нас нет такого пользователя')
#     else:
#         print('убедитесь что вы ввели правильную команду')




# name = "Ryan"



# def go_notgo(name):
#     name_example = "James"
#     if len(name) <= len(name_example):
#         return("Так уж и быть можеш дружить с {0}".format(name))
#     elif len(name) > len(name_example):
#         return f"Я бы не стал дружить с {name}"
# go_notgo(name)
