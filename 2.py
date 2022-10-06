from math import sqrt
katet1=int(input('Введите первый катет: '))
katet2=int(input('Введите второй катет: '))
gypotenyza=sqrt(katet1**2+katet2**2)
S=(katet1*katet2)/2
P=katet1+katet2+gypotenyza
print("Площадь треугольника = ", S)
print("Периметр треугольника = ", P)