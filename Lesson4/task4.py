#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

from random import randint

k=2
a2,a1,a0 = randint(0,100),randint(0,100),randint(0,100)
data = open ('task4.txt','a')
data.writelines('{}x^2 + {}x + {} = 0 \n'.format (a2,a1,a0))
data.close()


