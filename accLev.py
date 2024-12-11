level = 0   #Уровень доступа

login = ""
while not login:
    login = input("Введите логин: ")

password = ""
while not password:
    password = input("Введите пароль: ")

if login == "root" and password == "12345":
    level = 10
elif login == "mark" and password ==  "321":
    level = 5

if level:
    print("Привет, ", login)
    print("Ваш уровень доступа: ", level)
else:
    print("Доступ зарещен!")