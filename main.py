"""
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
"""

# 2) протипізувати перше завдання
from typing import Callable, List


def notebook() -> Callable:
    todo_list: List[str] = []
    note: str = input('Enter todo: ')

    def add_todo(todo: str) -> List[str]:
        nonlocal todo_list
        todo_list.append(todo)
        return todo_list

    def get_all() -> None:
        print(''.join(todo_list))

    add_todo(note)
    return get_all


case1 = notebook()
case2 = notebook()
case3 = notebook()
case4 = notebook()
case1()
case2()
case3()
case4()

"""
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""


def expanded_form(num: int) -> str:
    str_num = str(num)
    res: List[str] = []
    num_digit = len(str_num) - 1
    for i in str_num:
        if i != '0':
            res.append(i + '0' * num_digit)
        num_digit -= 1
    return ' + '.join(res)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

"""
4) створити декоратор котрий буде підраховувати скільки разів 
була запущена функція продекорована цим декоратором, 
та буде виводити це значення після виконання функцій
"""


def decor(func) -> Callable:
    count = 0

    def count_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'count: {count}')
        func()
        print('-' * 20)
    return count_func


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
