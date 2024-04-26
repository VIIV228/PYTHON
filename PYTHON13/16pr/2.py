def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fun(n, m):
    result = factorial(n) / (factorial(m) * factorial(n - m))
    return result

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
zn = fun(n, m)
print("Значение выражения:", zn)