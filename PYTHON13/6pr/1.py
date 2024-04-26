import math

n = int(input())
for i in range(n + 1):
    print("Корень число", i , "равен",  math.sqrt(i) )
    print("Квадрат числа", i, "равен", i * i)
    print("Куб числа", i, "равен", i * i * i)
