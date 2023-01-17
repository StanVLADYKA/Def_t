# 2 С помощью функции map вывести длину каждого элемента списка
# 3 Дан список чисел. Вернуть список, где каждое число переведено в строку [5, 3] -> [‘5’, ‘3’]
# 4 Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!'
# соответственно. Сделайте по одному вызову каждой из функций
# 5 Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!'
# соответственно. Выведите на экран 'Meow!' и 'Woof!' по 2 раза
# 6 Создайте функцию get_voice() которая возвращает передаваемый ей в качестве
# параметра текст c восклицательным знаком.

#2
res = list(map(len,("33","23","4444")))
print(res)

# 3
lst_ = [1,2,3,4,5,6]
res = list(map(str,lst_))
print(res)

# 4
def cat_voice():
    return 'Meow!'
def dog_voice():
    return 'Woof!'
print(cat_voice())
print(dog_voice())

# 5
def cat_voice():
    return 'Meow!'
def dog_voice():
    return 'Woof!'
print(cat_voice(),cat_voice())
print(dog_voice(),dog_voice())

# 6
def get_voice(text):
    return text + "!!!!"
print(get_voice("Hello"))
