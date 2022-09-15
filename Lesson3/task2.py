# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [2, 3, 4, 5, 6]
d = int(len(list))
n= int (d/2)
list1 =[]
if d%2!=0:
  for i in range (n+1):
    p = list[i]*list[-i-1]
    list1.append(p)
else:
    for i in range (n):
      p = list[i]*list[-i-1]
      list1.append(p)

print (list1)