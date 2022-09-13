# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число N => '))

numbers = []
for i in range(n+1):
    if i>0:
       numbers.append (round((1 + 1 / i)**i, 2))  
print (numbers)