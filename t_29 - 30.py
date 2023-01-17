# Используя функцию sorted() и lambda() - функцию, отсротируйте список кортежей
# по последнему символу их второго элемента

l_1 = [("Humans","have"),("always","been"),("drawn","to"),("explore","discover"),("and","learn"),
       ("as","much","as","we"),("can","about","the"),("world","and"),("worlds","around","us")]
l_2 = sorted(l_1,key=lambda x : x[1][-1])
print(l_2)

# Написать программу, сортирующую список словарей по значению некоторого общего ключа с помощью
# lambda - функции (например список сотрудников по возрасту)

# d_2 = [{age: 56:"Man 1"},{46:"Man 2"},{23:"Man 3"},{77:"Man 4"},{34:"Man 5"}]
d_2 = [{'name':'Homer', 'age':23}, {'name':'Bart', 'age':65},{'name':'Stan', 'age':39}, {'name':'Ant', 'age':33}]

d_3 = sorted(d_2,key = lambda x : x["age"])
print(d_3)