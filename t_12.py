# написать функцию, принимающую именнованные аргументы поэтов (фио, дата см и рожд, аннотация

def author(*args):
    if len(d_2) == 0:
        print(f" {fl}  ({d_1})   - {n}")
    else:
        print(f" {fl}  ({d_1}-{d_2}) - {n}")

fl = input("Full Name:  ")
d_1 = input("Born Date: ")
d_2 = input("Dad Date:  ")
n = input("Note:  ")

author(fl,d_1,d_2,n)