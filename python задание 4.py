a = int(input("Введите пятизначное целое число: "))
ones = a % 10
tens = (a // 10) %10
hundreds = (a // 100) % 10
thousands = (a // 1000) % 10
ten_thousands = (a// 10000) % 10
result = (tens**ones * hundreds) / (ten_thousands-thousands)
print("Результат: ", result)