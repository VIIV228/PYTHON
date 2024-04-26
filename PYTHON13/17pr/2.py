import random

exam = int(input("Количество экзаменов: "))

subject = input("Введите названия дисциплин через запятую и пробел: ").split(", ")

day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
time = [9.0 + 0.5 * i for i in range(10)]

for i in range(exam):
    days = random.choice(day)
    times = random.choice(time)
    ran = random.randint(1, 25)
    print(f"Экзамен по дисциплине «{subject[i]}» состоится в {days} время {times:.1f}. Ваш счастливый билет номер: {ran}.")