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