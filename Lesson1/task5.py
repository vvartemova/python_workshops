#Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

xa = int(input('Введите x точки А => '))
ya = int(input('Введите y точки А => '))
xb = int(input('Введите x точки B => '))
yb = int(input('Введите y точки B => '))
import math
result = math.sqrt((xa - xb)**2 + (yb - ya)**2)
print ((round(result, 2)))
