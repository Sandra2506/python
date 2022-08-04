#!/usr/bin/python3
def dank():
    a = int(input('Ведите кол-во денег:'))
    years = int(input("Введите кол-во лет:"))
    r = 10

    cnt = 0

    if a > 0 :
        for i in range(years):
            a = int(a+r*a/100)
            cnt += a
        print('Сумма денег:',cnt)
    else:
        print('Введите положительное число!')

dank()
