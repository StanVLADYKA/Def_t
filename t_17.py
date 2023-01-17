# дана последовательность целых чисел. Найти в каждом числе сумму четных цифр


def even(l):
    l_2 = []
    for i in l:
        l_2.clear()
        for b in str(i):
            if int(b) % 2 == 0:
                l_2.append(int(b))
        print("for num=",i," sum even =",sum(l_2))

l_1 = [888,6,5,11,23,28,76,17,98,101,44,19,4,44,496]

even(l_1)