# 7 Создайте функцию, которая генерирует последовательность нечетных чисел в
# диапазоне от a до b (a и b включительно). Значения a и b должны передаваться
# в качестве параметров. Результирующая последовательность должна возвращаться в
# форме объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него

# 8
# Создайте функцию is_cat_here(), которая принимает любое количество аргументов и проверяет
# есть ли строка 'cat' среди них. Функция должна возвращать True, если такой параметр есть
# и False в обратном случае. Буквы в строке 'cat' могут быть как большие, так и маленькие.

#9
# Создайте функцию is_item_here(item, *args), которая проверяет есть ли
# item среди args. Функция должна возвращать True, если такой параметр
# есть и False в обратном случае.

# 10
# Создайте функцию your_favorite_color() с позиционным параметром my_color
# и параметрами **kwargs, которая будет выводить на экран 'My favorite color is
# (значение my_color), what is your favorite color?',
# если в параметрах kwargs нет ключа color, и 'My favorite color is (значение my_color),
# but (значение по ключу color) is also pretty good!',
# если в параметрах kwargs ключ color присутствует

#7
def gen_seq(a,b):
    r = list(range(a,b,2))
    return r
print(gen_seq(3,77))

# List Comprehension:
def gen_seq(a,b):
    return [elem for elem in range(a,b) if elem%2 != 0]
print(gen_seq(3,77))


# nums = [elem **2 for elem in nums] -  exempl List Comprehension
# nums=[1,2,3,5,2]
# chars = ["a","f","e","e","y"]
# dc = [{elem:chars} for elem, char in nums for char in chars]
# print(dc)
# # # w3schools.com - site, примеры кодов и учебник


# 8
def is_cat_here(*args):
    l = [x.lower() for x in args]
    return "cat" in l

print(is_cat_here("home","red","doom","Cat"))


#9

def is_item_here(item,*args):
    return item in args

print(is_item_here(33, *(123,33,12,99)))

#10
def your_favorite_color(my_color,**kwards):
    print("what is your favorite color? - My favorite color is: ", my_color)
    for k,w in kwards.items():
        if k == "color":
            print("is also pretty good!  ", w)

your_favorite_color("yellow",dog = "good",fish = "wow",color = "red")