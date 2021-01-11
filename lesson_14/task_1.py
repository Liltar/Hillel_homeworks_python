# Написать программу кофейный магазин.
#
# Обьекты:
#
#    Product
#
#    - свойства: наименование, тип, цена
#    - print обьекта продукта должен возвращать прим. "Кофе: Эспрессо, цена: 27грн."
#
#
#    Store
#
#    - может импортировать продукты из файла invertory.csv
#    (по-умолчанию по 5 шт. каждого наименования)
#    - может вернуть список продуктов нужного типа (tea, coffee или все продукты)
#    - может вернуть общую стоимость продуктов в наличии
#    - может продать продукт
#
# *доп. Научить Store запоминать выручку(сумма проданных продуктов) и выводить баланс.
#
# Тип продукта может быть только coffee или tea (нельзя создать обьект с другим типом).
import csv


class Product:
    def __init__(self, name, product_type, price):
        self.name = name
        self.product_type = self._check_product_type(product_type)
        self.price = float(price)

    def __repr__(self):
        print(self.name, self.product_type, self.price)

    def _check_product_type(self, product_type):
        if product_type == 'tea':
            return 'tea'
        if product_type == 'coffee':
            return 'coffee'


class Store:
    def __init__(self):
        self.warehouse = self.read_inventory()
        self.transactions = []

    def read_inventory():
        with open('inventory.csv', 'r', encoding='utf-8') as inventory:
            csv_reader = csv.DictReader(inventory)
            result = []
            for row in csv_reader:
                result.append(row)
        return result

    def move_to_warehouse():
        with open('warehouse.csv', 'w', encoding='utf-8', newline='') as warehouse:
            fieldnames = ['Product', 'Quantity']
            writer = csv.DictWriter(warehouse, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Product': Store.read_inventory()[0], 'Quantity': 5})
            writer.writerow({'Product': Store.read_inventory()[1], 'Quantity': 5})
            writer.writerow({'Product': Store.read_inventory()[2], 'Quantity': 5})
            writer.writerow({'Product': Store.read_inventory()[3], 'Quantity': 5})
            writer.writerow({'Product': Store.read_inventory()[4], 'Quantity': 5})

    # def list_of_products_by_type(self, type):
    #     with open('warehouse.csv', 'r', encoding='utf-8', newline='') as warehouse:
    #         csv.reader = csv.DictReader(warehouse)
    #         result = []
    #         if
    #


print(Store.read_inventory()[0])
first_element = Store.read_inventory()[0]
print(first_element)
for key, value in first_element.items():
    print(key, value)

# Store.move_to_warehouse()