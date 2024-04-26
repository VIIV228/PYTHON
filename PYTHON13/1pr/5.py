print("Стоимость пирожка")
rub = int(input("Рублей:"))
kop = int(input("Копеек:"))
pie = int(input("Сколько пирожков:"))
price = rub * 100 + kop
summa = price * pie
price_rub = summa // 100 
price_kop = summa % 100
print("К оплате:",price_rub ,"руб.", price_kop,"коп.")