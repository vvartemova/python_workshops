#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите x => '))
y = int(input('Введите y => '))

if x>0 and y>0:
    print ('x = {}, y = {} -> 1'.format (x, y))
elif x>0 and y<0:
    print ('x = {}, y = {} -> 4'.format (x, y))
elif x<0 and y<0:
    print ('x = {}, y = {} -> 3'.format (x, y))
elif x<0 and y>0:
    print ('x = {}, y = {} -> 2'.format (x, y))
elif x==0 and y!=0:
    print ('x = {}, y = {} -> лежит на оси y'.format (x, y))
elif y==0 and x!=0:
    print ('x = {}, y = {} -> лежит на оси y'.format (x, y))