#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int (input ('Введите десятичное число => '))
number2 = ''

while number > 1:
   number2 = str(number%2) + number2
   number = number//2
   
 
print (str(number) + number2)