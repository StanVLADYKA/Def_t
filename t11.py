# программа проверки логина и пароля отдельной функцией (имя пользователя, пароль, к-во попыток (3)
# При неудаче сообщение: Система заблокирована, повторте через 5 мин.
# функция принимает логин, пароль и к-во попыток"


def input_lp(n):
    l = input("Input Login  :")
    p = input("Input Password  :")
    n = n + 1
    check(l, p, n)


def check(l,p,n):
    if l.isdigit() or p.isdigit() is True:
        print("only simbols,try again")
        if n == 3:
            print("Uncorrect, session stopped for 5 min")
        else:
            input_lp(n)

n = 0
t_ = input_lp(n)


