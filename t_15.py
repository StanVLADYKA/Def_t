# Дана последовательность целых чисел. Найти среднее арифметические совершенных чисел
# и среднее геометрические простых чисел.
# Совершенние число - это число, сумма всех делителей котроого, меньших его самого, равно самому числу

from statistics import mean, geometric_mean

def dig(l_1):
    l_2 = []
    l_5 = []
    for i in l_1:
        k = 0
        for a in range(2, i):
            if i % a == 0:
                k += 1
        if k <= 0:
            l_2.append(i)

        l_4 = []
        for b in range(1, i):
            if i % b == 0:
                l_4.append(b)
        if sum(l_4) == i:
            l_5.append(i)

    return l_2,l_5



l_1 = [6,5,11,23,28,76,17,98,101,44,19,4,44,496]

print(dig(l_1))
res = (dig(l_1))
print("среднее арифметические совершенных чисел:", mean(res[1]))
print("среднее геометрическое простых чисел:", geometric_mean(res[0]))

