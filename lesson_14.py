#pwd - показывает путь, где наход ваш файл 

# os.system('ls > ls.txt')

# list_ls = []
# list_code = ['py','html','txt','css']

# with open('ls.txt', 'r') as f:
#     f = f.read()
#     for i in f.split():
#         list_ls.append(i)
    
#     for passes in list_ls:
#         for j in passes.split('.'):
#             if j in list_code:
#                 os.system(f'mv {passes} /home/marselle/Рабочий\ стол/def\ main/lessons2')



# def file_passes():
#     list_file = ['Загрузки','Видео','Музыка','Рабочий\ стол','Изображения']
#     for i in range(1):
#         for passes in list_file:
            
#     os.system('cd')
#     time.sleep(1)
#     os.system(f'cd {passes}')
#     time.sleep(1)
#     os.system('ls > list.txt')
        
        
# import os, time
        

# def download_passes():
#     list_file = []
#     list_expansion = ['.png', 'jpg', 'jpeg']
#     os.system('cd /home/Загрузки')
#     os.system('ls /home/Загрузки > /home/Рабочий\ стол/def\ main/list.txt')
#     time.sleep(1)
#     with open('list.txt', 'r') as file:
#         ls_download = file.read()
#         for name_file in ls_download.split():
#             print(name_file)
        
        
#         for items in ls_download.split('.'):
#             p = items.split()
#             if p in list_expansion:
#                 os.system(f'mv {items} /home/marselle/Изображения')
#             else:
#                 continue
                
                
#             # if item in list_expansion.split('.'):
# print(download_passes())



# def main(x, y):
#     return x+y
# print(main(1, 2))

# l =lambda x, y =10 : x+y
# print(l(1))



# while True:
    
#     table = input("""
#         +    1
#         -    2
#         /    3
#         *    4
#         num  5
#     """)
#     if table =="1":
#         num = int(input("Enter number: "))
#         num1 = int(input("Enter number: "))
#         res = lambda x , y: x+y
#         print(res(num, num1))
#     elif table == "2":
#         um = int(input("Enter number: "))
#         num1 = int(input("Enter number: "))
#         res = lambda x , y: x-y
#         print(res(num, num1))
#     elif table =="3":
#         um = int(input("Enter number: "))
#         num1 = int(input("Enter number: "))
#         res = lambda x , y: x/y
#         print(res(num, num1))
#     elif table =="4":
#         num = int(input("Enter number: "))
#         num1 = int(input("Enter number: "))
#         res = lambda x , y: x*y
#         print(res(num, num1))
#     elif table =="5":
#         num = int(input("Enter number: "))
#         res = lambda x =num, y=num : x*y
#         print(res(num))



# a = [1, 2, 3, 4]
# l = list(map(lambda x: x*x, a)) #  map - показ путь к значание 
# print(l)

# l = list(filter(lambda x: x%2 == 0, [1,2,3,4])) # filter - показывает определенные обьекты 
# print(l)

# def mf():
#     m =12.3
#     return int(m)

# print(mf())

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def man(lists):
#     for i in range(1, len(list1)):
#         for j in range(i, len(list1)):
#             if i % 2 == 0 and j % 2 == 1:
#                 if list1[j]<list1[i]:
#                     num = list1[i]
#                     list1[i] = list1[j]
#                     list1[j] = num
#     return list1
# print(man([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))



# name = ["Ryan", "Kieran", "Jason", "Yous", "Jon", "Spanser", "Tomos", "Mark"]
# test = []


# for i in name:
#     if len(i) <= len(name[0]):
#         test.append(i)
#         for k in range(3, len(test)):
#             print(test)
# print(name)


# name = ["Ryan", "Kieran", "Jason", "Yous", "Jon", "Spanser", "Tomos", "Mark"]
# def go_notgo(name):
#     task = []
#     name_example = ["Ryan"]
#     for i in name_example:
#         for j in name:
#             if len(j) <= len(i):
#                 task.append(j)
#                 for k in range(3, len(task)):
#                     return(task)
# print(go_notgo(name))


# from lesson_13 import go_notgo

# while True:
#     step = input("""
#         Играть жми - 1
#         Надоело жми - 2
#         """ )
#     if step == "1":
#         name = input("Введите имя вашего друга а я подумаю : ")
#         rezalt = go_notgo(name)
#         print(rezalt)
#     elif step == "2":
#         print("Наконец-то мы закончили, и так дел полно")
#         break
#     else:
#         print("Только 1 или 2, гений")
    
