#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = [1.12, 1.25, 3.1, 5, 10.01]

list1 = []
for i in range (len(list)):
    p = list[i] - int(list[i])
    m = round (p,3)
    list1.append(m)
print (list1)
result = max(list1) - min(list1)
print (result)