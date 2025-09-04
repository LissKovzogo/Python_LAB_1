#! Вычисление факториала
print("Поиск факториала числа: ")
number = 10
result = 1
for i in range(1,number+1):
    result *= i
print("Факториал ", number," = ", result)