



path = 'task5-1.txt'
data = open (path,'r')
for line in data:
    a = line
data.close ()

path = 'task5-2.txt'
data = open (path,'r')
for line in data:
    b = line
data.close ()
print(a)
print (b)
print (a.find('x^2'))
a2 = a[:a.find('x^2')]
a = a [:]
b2 = b[:b.find('x^2')]
print(b2)
a1 = a[a.find('x^2 +'):a.find('x')]
print(a1)
