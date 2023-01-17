# 1 написать рекурсивную функцию подсчета суммы элементов списка чисел

def sum_rec(l):
    if not l:
        return 0
    else:
        return l[0] + sum_rec(l[1:])

ln = [22,33,12,78,9]
print(sum_rec(ln))

# 2 Написать рекурсивную функцию подсчета суммы цифр положительного целого числа

def sum_rec_2(n):
    if len(n) == 0:
        return 0
    else:
        return int(n[0]) + sum_rec_2(n[1:])

print(sum_rec_2("456"))

# 3 Написать рекурсивную функцию подсчета суммы первых n членов гармоничного ряда (с 1 для N) шаг 1/k

def sum_rec_3(n):
    if n == 0:
        return 0
    else:
        return 1/n + sum_rec_3(n-1)

print(sum_rec_3(9)) # кол-во первых членов