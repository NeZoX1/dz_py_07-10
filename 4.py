years=int(input("Введите количество лет: "))
days=years*365
hours=days*8
minutes=60*hours
exp=minutes/5
print("За это количество лет можно просмотреть", int(exp), "экспонатов")
exp=int(input('Введите количество экспонатов: '))
years=((exp*5/60)/8)/365
hours=exp*5/8
minutes=exp*5
print("Для просмотра", exp, "экспонатов понадобится:",years, "лет/год.", "или", days, "дн.", "или", hours, "ч.", "или", minutes, "мин.")


