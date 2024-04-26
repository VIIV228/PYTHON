numbers = [22, 33, 44, 55, 66, 77, 88, 99, 110, 121]

result = [num for num in numbers if num % 2 != 0 and num % 11 == 0]

print("Нечетные числа, делимые на 11 из исходного списка:")
print(result)
