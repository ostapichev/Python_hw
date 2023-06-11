"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли
з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
"""

with open('emails.txt') as file:
    content = file.read()
    emails = content.split()
with open('gmails.txt', 'w') as new_file:
    [new_file.write(f'{gmail}\n') for gmail in emails if gmail[-9:] == 'gmail.com']

"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""

import json
from pprint import pprint


purchases = [
    {'id': 1, 'product': 'TV', 'price': 15000},
    {'id': 2, 'product': 'washing machine', 'price': 12000},
    {'id': 3, 'product': 'laptop', 'price': 30000},
    {'id': 4, 'product': 'toaster', 'price': 1200},
    {'id': 5, 'product': 'microwave', 'price': 5500},
    {'id': 6, 'product': 'fridge', 'price': 20000},
]

file_name = 'purchases.json'
with open(file_name, 'w') as f:
    json.dump(purchases, f)

with open(file_name) as f:
    purchase = json.load(f)
    pprint(purchase)

product_name = input('Enter a product')
price = input('Enter a price')


"""
*********Кому буде замало ось завдання з співбесіди
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку

в результат має записатись тільки 5 id

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122]"""
