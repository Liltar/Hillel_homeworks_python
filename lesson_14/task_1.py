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

    def _check_product_type(self, product_type):
        if product_type == 'tea':
            return 'tea'
        if product_type == 'coffee':
            return 'coffee'

    def print_product(self):
        if self.product_type is not None:
            print(f'{self.name}, {self.product_type}, {self.price} uah')
        else:
            pass


class Store:
    def __init__(self):
        self.warehouse = []
        self.transactions = []

    def inventory(self):
        with open('inventory.csv', 'r', encoding='utf-8') as inventory:
            reader = csv.DictReader(inventory)
            for row in reader:
                self.add_product(row, 5)

    def add_product(self, row, quantity):
        product = Product(row['Наименование'], row['Тип'], row['Цена'])
        self.warehouse.extend([product] * quantity)

    def print_products(self):
        for products in self.warehouse:
            products.print_product()

# корректно не работает, выдаёт список вида [<__main__.Product object at 0x000001D25E628970>,
    # <__main__.Product object at 0x000001D25E628970> и так далее]
    def get_products_by_type(self, product_type):
        products_filtered = []
        for product in self.warehouse:
            if product.product_type == product_type:
                products_filtered.append(product)
        print(products_filtered)

    def total_cost(self):
        cost = 0
        for product in self.warehouse:
            cost += product.price
        return cost

    def sell(self, product):
        if product in self.warehouse:
            self.warehouse.remove(product)
            self.transactions.append(product)
        else:
            raise Exception('No way!')

    def calc_revenue(self):
        revenue = 0
        for transaction in self.transactions:
            revenue += transaction.price
        return revenue

    def add_new_product(self, product):
        self.warehouse.append(product)


my_store = Store()
my_store.inventory()
print(my_store.total_cost())
mokko = Product('Мокко', "coffee", 45.0)
my_store.add_new_product(mokko)
print(my_store.total_cost())
my_store.sell(mokko)
print(my_store.calc_revenue())
my_store.get_products_by_type('coffee')