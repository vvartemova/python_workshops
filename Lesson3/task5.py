#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n in (1, 2):                       
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def negafibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        fib1, fib2 = 1, -1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 - fib2
        return fib2

list = [0]
number = int(input('Введите число => '))
for i in range(1, number + 1):
    list.append(fibonacci(i))
    list.insert(0, negafibonacci(i))
print(list)