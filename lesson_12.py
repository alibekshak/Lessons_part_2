# git init  
# git remote add origin ...(copy u)  
# git checkout -b ...(name)
# git add .
# git commit -m ''
# git push -u origin ...(name)


# def main(x, y):
#     return(x+y) # возвращает функуию 

# print(main(5, 6))# - указываем аргументы 


# def leng(a):
#     n = 0
#     try:
#         a =str(a)
#         for i in a:
#             n+=1
#             return n
#     except:
#         print("Error")


# print(leng("asdfqwer"))


# def adi(a, b=1):
#     return(a+b)

# print(adi(10))


# def calculator(oper, num, num1):
#     if oper == "+":
#         return num + num1
#     elif oper == "-":
#         return num - num1
#     elif oper == "*":
#         return num * num1
#     elif oper == "/":
#         return num / num1
#     elif oper == "**":
#         return num ** num1
#     return "Error"

# print(calculator("+", 2, 4))


#1

# def random(num_list: list, size_list: int, min_n: int, max_n:int):
#     from random import randint
#     for i in range(size_list):
#         num_list.append(randint(min_n, max_n))

# n = []
# min = int(input("Min: "))
# max = int(input("Max: "))
# size = int(input("Size_l: "))
# random(n, size, min, max)
# print(n)


#2
# a = int(input("start: "))

# def Fib(s):
#     a, b=0, 1
#     for i in range(s):
#         yield a
#         a, b=b, a +b
# print(list(Fib(a)))


#3
# def rev(a):
#     a = a.split()
#     a.reverse()
#     return " ".join(a)
# print(rev(input("Enter: ")))


#4 

# from random import randint

# def random_num(max_num = 100):
#     l = []
#     for i in range(max_num):
#         l.append(randint(1,max_num))
#     return l

# max_num = int(input("size "))
# print(random_num(max_num))



a = int(input("Num: "))
b = int(input("Num: "))

def calc (num, num1):
    return num + num1, num - num1, num / num1, num * num1
res1, res2, res3, res4 = calc(a, b)

print(res1, res2, res3, res4)


