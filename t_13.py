# написть функция, принимает произвольное к-во целых чисел, определить сколько в них 2-зн
# и 3 - зн. цифр.
# определение разрядности оформить отдельной функцией

def int_num(*args):
    num = [n for n in args]
    return num


def mult(n):
    n_2 = 0
    n_3 = 0
    for i in n:
        if len(str(i))  == 2:
            n_2 += 1
        if len(str(i))  == 3:
            n_3 += 1
    return print("two digids", n_2, "  three digids:", n_3)



na = int_num(3,44,55,234,777,88,222,33,44,5555,6,77,99)
mult(na)

