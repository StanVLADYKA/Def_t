# дана последовательность целых чисел. Для каждого числа найти к-во его делителей


def deno(l):
    for i in l:
        s=0
        for d in range(1,i+1):
            if i % d == 0:
                s += 1
        print("for number ",i,"number of divisors: ",s)

l_1 = [6,5,11,23,28,76,17,98,101,44,19,4,44,496]
deno(l_1)