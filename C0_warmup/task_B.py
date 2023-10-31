a, b, c, d = map(int, input().split())


def GCD(a, b):
    '''поиск Наибольшего Общего Делителя по алгоритму Евклида'''
    return a if b == 0 else GCD(b, a % b)


def LCM(a, b):
    '''поиск Наименьшего Общего Кратного'''
    return int((a*b)/GCD(a, b))


e = LCM(b, d)

numerator = a*e/b + c*e/d
denominator = int(e / GCD(e, numerator))
numerator = int(numerator / GCD(e, numerator))
print(numerator, denominator)
