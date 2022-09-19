#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

input_numbers = []
output_numbers =[]
for i in range(10):
  i = int(input('Введите число '))
  input_numbers.append(i)
  if i  not in output_numbers:
    output_numbers.append(i)
print (input_numbers)
print(output_numbers)