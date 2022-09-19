#Вычислить число c заданной точностью d

from math import pi

def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1
    
d =  float (input('Задайте точность числа Пи => '))
n = num_after_point (d)
print (n)
if  10**(-1) >= d >= 10**(-10):
  print(f'число Пи с точностью {d} равно {round(pi, n)}')
else:
    print ('Точность задана некорректно')