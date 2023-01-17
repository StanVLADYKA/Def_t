# 1 Дан список слов. Отфильтровать список с использованием Lambda - функции,
# оставив в нем только слова - палиндромы

l = ["потоп", "репка","радар","дед","праздник"]

res = filter(lambda x : x =="".join(reversed(x)),l)
print(list(res))


# 2 Дан список чисел. Используя lambda- функцию, возведите в квадрат и в куб все элементы данного списка

ln = [22,33,12,78,9]


ln_2 = list(map(lambda x: x**2,ln))
ln_3 = list(map(lambda x: x**3,ln))

print(ln_2,ln_3)