#aregs

# list1 = [1, 2, 3, 4, 5 ]
# a = [*list1, 7, 8, 9, ]
# print(a)

# def test (name, *s):
#     return f"Hi {name} good {s}"

# print(test("Bob", True, False))


#kwargs - создает dict
# def kwargs(**kwargs):
#     baza = ["login" ]
#     return baza.append(kwargs.items())
# print(kwargs(name = "Jon", age = 12, job = "program", num = 12))

# number = 12
# v = str(number)
# print(v)


#recurs
# 7!
# 1*2*3*4*5*6*7 = 7!
# def test(a):
#     a += 1
#     print(a)
#     return test1(a)

# def test1(a):
#     a += 1
#     print(a)
#     return test(a)

# print(test(1))


# def test2():
#     return test2()
# test2()


def defind_factorial(num): #factorial
    if num == 1:
        return num
    else:
        return num * defind_factorial(num-1)
print(defind_factorial(6))


#dicorator
# функуции в пайтоне является обьектом

# def object_fuction(name):
#     return f"Hi {name}"
# hellow_name = object_fuction("Jon") 

# print(hellow_name)

# def hellow_name(name):
#     return name

# def main_decorator(funct):
#     def decor():
#         a = input("Name: ")
#         funct()
#         return a
#     return decor
    

# @main_decorator
# def hellow():
#     for i in range(1, 10+1):
#         return i 

# print(hellow())
# def hellow_name():
#     print ("Jon")

# get_main = main_decorator(hellow_name)
# get_main()

# def hello_name2():
#     print("1234567890")
# hello_name2()


# def main_get(food):
#     def def_decorator():
#         food()
#         print("beaf", "carret", "apple")
#     return def_decorator

# @main_get#обертка
# def main():
#     print("Good job")

# main()

#decorator - дополнит функиции, дополняет основн фунцию без изменения основной код функции
# def main_get(name_people):
#     def def_decorator(last_name, firt_name):
#         print(f"Hi {last_name} {firt_name}")
#         name_people(last_name, firt_name)
#     return def_decorator

# @main_get
# def  name_people(last_name, firt_name):
#     print(f"My name is {firt_name} {last_name}")

# name_people("Guver", "Jon")



#1
# r=lambda x, y, z: x*y*z
# print(r(2,3,4))


#2
# import datetime

# def new_year(day, month, year):
#     a = int(datetime.datetime.today().strftime("%d"))
#     b = int(datetime.datetime.today().strftime("%m"))
#     c = int(datetime.datetime.today().strftime("%Y"))
#     return f"{day - a}дней {month - b}месцев {year -c}лет до Нового года"
# print(new_year(26, 12, 2023))


#3
# def main(a, n=1):
#     if n>a:
#         return
#     else:
#         print(n, end= " ")
#         main(a, n+2)
# main(13)


