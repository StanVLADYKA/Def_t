#1  написать функцию, принимающая произвольное кол-во целых чисел и возвращающую наибольшее
# положительное из них кратное 13



#1
def d_13(*args):
    l = []
    for i in args:
        if i % 13 == 0 and i > 0:
          l.append(i)

    return (print(max(l)))

d_13(2,44,26,13,17)


#2  написать функцию, принимающая инф. о геометрической фигуре и рассчитывающую площадь данноф фигуры
# (на примере квадрата треуг)
def sq(a,b,c=0):
    if c == 0:
        s = a*b
    if c !=0:
        p = p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
    return (print(s))

sq(12,10,8)
# sq(12,10)