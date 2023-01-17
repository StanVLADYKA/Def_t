# 1 написать функцию, которая принимает один аргумент, который в дальнейшем будет умножаться
# на заданное число

def mult(n):
    return lambda x: x * n

f = mult(33)
print(f(22))

# 2 написать программу, в котрой с помощью функции sorted() и lambda - функции отсортировать
# слова в списке по их второй букве

l_1 = ["Humans","have","always","been","drawn","to","explore","discover","and","learn","as","much","as","we","can","about","the","world","and","worlds","around","us"]
l_2 = sorted(l_1,key=lambda x : x[1])
print(l_2)

# 3 Написать программу, проверяющую, начинается ли заданная строка с заданного символа,
# с помощью lambda - функции

st_1 = "make history by sending the first humans to explore the region near the lunar South Pole"

c_1 = lambda s : s == st_1[0]
print(c_1("v"))
