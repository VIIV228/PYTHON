import string
import random

def pass_1(number, length):
    pass_2 = set()
    while len(pass_2) < number:
        pass_2.add(passwordd(length))
    return pass_2

def passwordd(length):
    char = string.ascii_letters + string.digits
    password = ''.join(random.choice(char) for _ in range(length))
    return password

number = int(input("Количество паролей: "))
length = int(input("Длина пароля: "))

passwords = pass_1(number, length)
for password in passwords:
    print(password)