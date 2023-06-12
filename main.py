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


class Purchase:
    FILE = 'purchases.json'

    def __init__(self, product, price, id):
        self.product = product
        self.price = price
        self.id = id
        self.purchases = []
        self.save_purchases()

    def load_purchase(self):
        try:
            with open(Purchase.FILE) as f:
                self.purchases = json.load(f)
        except FileNotFoundError:
            pass

    def save_purchases(self):
        purchases_data = self.to_dict()
        self.load_purchase()
        self.purchases.append(purchases_data)
        with open(Purchase.FILE, 'w') as f:
            json.dump(self.purchases, f, indent=4)

    def get_all_purchases(self):
        return self.purchases

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.product,
            'price': self.price
        }

    def __str__(self):
        return f'id: {self.id} product: {self.product} price: {self.price}'


def load_all():
    try:
        with open(Purchase.FILE) as f:
            purchases = json.load(f)
            for purchase in purchases:
                string = str(purchase)
                new_string = string.replace('{', '').replace('}', '')
                print(new_string)
    except FileNotFoundError:
        pass


def write_note():
    product = input('Enter a product ')
    price = float(input('Enter a price '))
    id = int(input('Enter id '))
    Purchase(product, price, id)


def search_in_json(file_path, search_value, search_key='name'):
    results = []
    with open(file_path) as f:
        data = json.load(f)
        for item in data:
            if search_key in item and item[search_key] == search_value:
                results.append(item)
    return results


def get_expensive():
    with open(Purchase.FILE) as f:
        purchases = json.load(f)
    if not purchases:
        return None
    print(max(purchases, key=lambda purchase: purchase['price']))


def del_purchase(id):
    with open(Purchase.FILE) as f:
        data = json.load(f)

    deleted_id = []
    updated_data = []
    for item in data:
        print(item['id'])
        if item['id'] != int(id):
            updated_data.append(item)
        else:
            deleted_id.append(item)

    with open(Purchase.FILE, 'w') as f:
        json.dump(updated_data, f, indent=4)

    return deleted_id


while True:
    print('1. Show all purchases')
    print('2. Add purchase to Book')
    print('3. Search a purchase')
    print('4. Show a most expensive')
    print('5. Delete a purchase')
    print('6. Exit')
    choice = input('Mke your choice ')

    match choice:
        case '1':
            load_all()
        case '2':
            write_note()
        case '3':
            value = input('value ')
            search_results = search_in_json('purchases1.json', value)
            if search_results:
                for result in search_results:
                    print(result)
            else:
                print("No results found.")
        case '4':
            get_expensive()
        case '5':
            del_id = input('Enter removed ID: ')
            removed_ids = del_purchase(del_id)
            if removed_ids:
                print("Removed items:")
                for item in removed_ids:
                    print(item)
            else:
                print("No items found for removal.")
        case '6':
            break

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
