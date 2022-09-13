#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

n = int(input('Введите число N => '))
numbers = []

for i in range(n+1):
    if i>0:
       numbers.append (factorial(i))
  
print (numbers)