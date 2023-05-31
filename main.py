# strings

"""
1) написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад: st = 'as 23 fdfdg544' введена строка 2,3,5,4,4 вивело в консолі.
"""
st = 'as 23 fdfdg544'
list_num = [int(i) for i in st if i.isdigit()]
print(list_num)

"""
2) написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад: st = 'as 23 fdfdg544 34' #введена строка 23, 544, 34 вивело в консолі
"""
st2 = 'as 23 fdfdg544 34'
list_num2 = []
str_num = ''
for i in st2:
    if i.isdigit():
        str_num += i
    elif str_num:
        list_num2.append(str_num)
        str_num = ''
if str_num:
    list_num2.append(str_num)

list_result = [int(i) for i in list_num2]
print(list_result)

# list comprehension
"""
1) є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""
greeting = 'Hello, world'
list_greeting = [s.upper() for s in greeting]
print(list_greeting)

"""
2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""
list_num3 = [i ** 2 for i in range(51) if i % 2]
print(list_num3)


# - створити функцію яка виводить ліст
def get_list(*args):
    return list(args)


array = get_list(1, 2, 3, 5, 8)
print(array)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def get_max(a, b, c):
    return max(a, b, c)


max_num = get_max(2, 1, 23)
print(max_num)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def get_max_args(*args):
    return max(args)


max_args = get_max_args(8, 3, 9, 22, 15)
print(max_args)


# - створити функцію яка повертає найбільше число з ліста
def get_max_list(nums):
    return max(nums)


number = [3, 6, 10, 34, 8, 21]
max_list = get_max_list(number)
print(max_list)


# - створити функцію яка повертає найменьше число з ліста
def get_min_list(nums):
    return min(nums)


number = [3, 6, 10, 34, 8, 21]
min_list = get_min_list(number)
print(min_list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def get_num_list(nums):
    return sum(nums)


number = [3, 6, 10, 34, 8, 21]
sum_list = get_num_list(number)
print(sum_list)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def get_avg_list(nums):
    return sum(nums) // len(nums)


number = [3, 6, 10, 34, 8, 21]
avg_list = get_avg_list(number)
print(avg_list)

"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
"""
list_nums = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
min_num = min(list_nums)
del_duplicate = set(list_nums)

count_x = len(list_nums) // 4
list_x = []

for x in range(count_x):
    list_x.append('X')

list_nums[3::4] = list_x

print(min_num)
print(del_duplicate)
print(list_nums)

"""
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
"""


def print_stars(count_stars):
    print('*' * count_stars)


def print_space(count_space):
    print('*', ' ' * count_space, '*')


def print_row(row, space_count):
    for i in range(row):
        print_space(space_count)


def print_square(stars, space, row):
    print_stars(stars)
    print_row(row, space)
    print_stars(stars)


print_square(10, 6, 8)

"""
3) вывести табличку множення за допомогою цикла while
"""


count = 0
while count < 9:
    count += 1
    for i in range(1, 10):
        num_table = i * count
        print(f'{num_table:4d}', end='')
    print()

"""
4) переробити це завдання під меню
"""
