import random
import math

for _ in range(10):
    num = random.randint(-10, 10)
    
    if num < 0:
        print(f"Число {num} отрицательное, пропускаем вычисление квадратного корня.")
        continue
    
    if num == 0:
        print("Ноль обнаружен, завершаем выполнение цикла.")
        break
    
    square_root = math.sqrt(num)
    print(f"Квадратный корень числа {num} равен {square_root}")
