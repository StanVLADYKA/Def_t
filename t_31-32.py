# напишите программу, которая будет считать к-во четных и нечетных чисел в заданном списке
#  с помощью lambda - функции

l = [23,11,23,45,6,77,8,9,23,445,67,98,543,2,3,55,1,9000]

l_1 = filter(lambda x: x%2 == 0, l)
l_2 = filter(lambda x: x%2 != 0, l)

print(list(l_1),"\n",list(l_2))

# напишите программу, которая будет складывать соответсвующие элементы заданных списков чисел
#  с помощью функций map и lambda функции. Например: для списков [1,2,3] и [4,5,6]
#  результатом будет [5,7,9]

l_3 =  [23,11,23,45,6,77,8,9,23]
l_4 =  [2,4,3,5,8,77,8,9,23]

l_5 = list(map(lambda x, y : x+y, l_3,l_4))
print(l_5)