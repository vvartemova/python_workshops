#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

list = [2, 3, 5, 9, 3]
sum = 0
for i in range (len(list)):
    if i%2 != 0:
       sum +=list[i]
print (sum)
