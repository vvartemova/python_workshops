# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def logical_check (x,y,z):
    left_part = not(x or y or z)
    right_part = (not x) and (not y) and (not z)
    print (left_part == right_part)


logical_check (0,0,0)
logical_check (1,0,0)
logical_check (0,1,0)
logical_check (0,0,1)
logical_check (1,1,0)
logical_check (1,0,1)
logical_check (0,1,1)
logical_check (1,1,1)

