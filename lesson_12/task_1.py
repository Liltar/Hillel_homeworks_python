# 1. Описать класс "Банковский счет", атрибуты у которого:
#        имя аккаунта - str
#        уникальный id (uuid)
#        баланс float
#        транзакции (список)
#
#    Методы
#         депозит средств
#         вывод средств
#         получить баланс
#
#    При изменении баланса записывать в транзакции (сумма, тип операции, текущая_дата)
#
#    * доп. добавить и учитывать банковские комиссии (1%)

class Bank_account():
    def __init__(self):
        acc