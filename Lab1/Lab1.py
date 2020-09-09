import math
import sys

print('Назаров Максим Михайлович ИУ5-53Б')

if len(sys.argv) == 4:
    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        C = int(sys.argv[3])
    except:
        print('Ошибка ввода параметра, введено не целое число.')
        sys.exit (0)
else:
    while True:
        try:
            A = int(input('Введите параметр A: '))
        except:
            print('Ошибка, введено не целое число. Повторите попытку')
            continue
        break
    while True:
        try:
            B = int(input('Введите параметр B: '))
        except:
            print('Ошибка, введено не целое число. Повторите попытку')
            continue
        break
    while True:
        try:
            C = int(input('Введите параметр C: '))
        except:
            print('Ошибка, введено не целое число. Повторите попытку')
            continue
        break

if A != 0 and B != 0 and C != 0:
    D = B**2-4*A*C
    if D > 0:
        Y1 = (-B+math.sqrt(D))/(2*A)
        Y2 = (-B-math.sqrt(D))/(2*A)
        if Y1 >= 0 and Y2 >= 0:
            X1 = math.sqrt(Y1)
            X2 = math.sqrt(Y2)
            X3 = -(math.sqrt(Y1))
            X4 = -(math.sqrt(Y2))
            print('X1='+str(X1), 'X2='+str(X2), 'X3='+str(X3), 'X4='+str(X4))
        elif Y1 >= 0 and Y2 < 0:
            X1 = math.sqrt(Y1)
            X2 = -(math.sqrt(Y1))
            print('X1='+str(X1), 'X2='+str(X2))
        elif Y1 < 0 and Y2 >= 0:
            X1 = math.sqrt(Y2)
            X2 = -(math.sqrt(Y2))
            print('X1='+str(X1), 'X2='+str(X2))
        else:
            print('Нет корней')
    elif D == 0:
        Y1 = (-B)/(2*A)
        if Y1 > 0:
            X1 = math.sqrt(Y1)
            X2 = -(math.sqrt(Y1))
            print('X1='+str(X1), 'X2='+str(X2))
        elif Y1 == 0:
            print('X=0')
        else:
            print('Нет корней')
    else:
        print('Нет корней')
elif A != 0 and B == 0 and C == 0:
    print('X=0')
elif A == 0 and B != 0 and C == 0:
    print('X=0')
elif A == 0 and B == 0 and C != 0:
    print('Нет корней')
elif A == 0 and B != 0 and C != 0:
    D = -C/B
    if D > 0:
        X1 = math.sqrt(D)
        X2 = -(math.sqrt(D))
        print('X1='+str(X1), 'X2='+str(X2))
    elif D == 0:
        print('X=0')
    else:
        print('Нет корней')
elif A != 0 and B == 0 and C != 0:
    D = -C/A
    if D > 0:
        D = math.sqrt(D)
        X1 = math.sqrt(D)
        X2 = -(math.sqrt(D))
        print('X1='+str(X1), 'X2='+str(X2))
    elif D == 0:
        print('X=0')
    else:
        print('Нет корней')
elif A != 0 and B != 0 and C == 0:
    Y1 = -B/A
    Y2 = 0
    if Y1 > 0:
        X1 = math.sqrt(Y1)
        X2 = -(math.sqrt(Y1))
        print('X1='+str(X1), 'X2='+str(X2), 'X3=0')
    else:
        print('X=0')
else:
    print('Любое число является корнем')
