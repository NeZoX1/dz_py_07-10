A=input("Введите имя: ")
B=input("Введите фамилию: ")
C=input("Введите год рождения: ")
print(A, B, C)
A, B, C = B, A, int(C)
C=C+60
print(A, B, C)