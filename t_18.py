# дана последовательность целых чисел. Для каждого числа последовательности проверить,
# представляют ли его цифры строго возрвстающую последовательность


def sequence(l):
    l_2 = []
    for i in l:
        i = str(i)
        if len(i) == 1:
            continue
        l_2.append(i)
        for a in range (0,len(i)-1):
            if i[a+1] > i[a]:
                pass
            else:
                l_2.pop()
                break
    print("Числа из списка содержащие строго возрвстающую последовательность цифр: ",l_2)


l_1 = [56789,66,58,1,4,13,88,5,6,889,99,10,111,123,1000,2222,456,3000,7000000,70000001,6789]
sequence(l_1)