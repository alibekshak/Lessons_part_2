#1
number = int(input("Number: "))
number1 = int(input("NUmber: "))
v = input("+, -, /, *, **, %:")
name = input("Name: ")

if v == "+":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}+{number1} = {number+number1}")

elif v == "-":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}-{number1} = {number-number1}")
    
elif v == "*":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}*{number1} = {number*number1}")
    
elif v == "/":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}/{number1} = {number/number1}")

elif v == "**":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}**{number1} = {number**number1}")

elif v == "%":
    with open("game.txt", "w") as f:
        f.write(f"{name} сделал спрос на {number}%{number1} = {number%number1}")


#2

users = {
    'Guluzim':{
        'login': 'Guluzim',
        'password':'12345'
} }

key = None
while True:
    x = input(''' выберите действие :  
1 РЕГИСТРАЦИЯ
2 ВХОД
3 СПИСОК 
4 ВЫХОД
 ''')
    if x == '1':
        if key is None:
            login = input(' login : ')
            password = input('passeord: ')
            users.setdefault (login) 
            users.update({
                                login : {
                                    'login': login,
                                    'password': password
                                }
            })

    elif x == '2':
        if key is None:
            login = input(' login : ')
            password = input('password: ')
            if login in users.keys():
                if password == users[login]['password']:
                    key = login
                    print(f'ДОБРО ПОЖАЛОВАТЬ ! {login}')
                else : 
                    print('Данные введены неправильно!, попробуйте еще раз ')
                    True
    elif x == '3':
        print(users.keys())
    elif x == '4':
        print(f'всего хорошего {login}')

#3
dict = {
    "a":5,
    "b":3,
    "c":10,
    "d":15,
    "e":20,
    "f":30,
    "g":42,
    "h":50
}


f = dict.values()
d = list(f)
print(d)
for i in d:
    if i % 3 == 0:
        print("Hi")
    elif i % 5 == 0:
        print("Bye")

#4
sum = 0
x = 1000
y = list(range(1, x))
for i in range(x - 1):
    if (y[i] % 3 == 0) or (y[i] % 5 == 0):
        sum += y[i]
print(sum)

#5

a = "4729461084"
c = list(map(int, a))
print(c)
print(sum(c))


#6
date ={
    
        }
year = input('year:')
month = input('month: ')
day = input('day : ')

date['year'] = year
date ['month'] = month
date ['day'] = day

print(date)

#7
words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
for i in words:
    if str(i) == "".join(reversed(i)) :
        print("Palindrome")
    else:
        print("Not Palindrome")



#Final
citybaza = ['New York', 'London']
key = None
while True:
    x = input('''

            Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
''')
    if x == '1':
        if key is None:
            city = input('введите город : ')
            if city not in citybaza and city.isalpha() :
                citybaza.append(city)
                print(citybaza)
                print('город добавлен ! ')
                key = city
            else :
                print('такой город уже есть в списке ')
            
    if x == '2':
        print(citybaza, end="\n")

    if x == '3':
        if key is not None:
            newcity = input('введите новый город : ')
            if newcity not in citybaza:
                citybaza.remove(city)
                citybaza.append(newcity)
                print(citybaza)
            else:
                print('такой город уже существует ')
        
        else : 
            print('gorod otsutstvuiet ')
            True


    if x == '4':
         city = input("Какой город удалить:")
         citybaza.remove(city)
         print(citybaza)

    if x == '5':
        break