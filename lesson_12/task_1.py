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
import time
import uuid


# какой функцией указать время события так, чтобы оно не сдвигалось каждый раз?


def commission(amount):
    return amount * 0.01


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.unique_id = uuid.uuid1()
        self._balance = 0.0
        self.transactions = []

    def make_depo(self, sum_of_depo):
        sum_of_depo = float(sum_of_depo) - commission(sum_of_depo)
        time_of_depo = time.monotonic()
        self.transactions.append(f'deposit of {sum_of_depo} made at {time_of_depo}')
        self._balance += sum_of_depo

    def withdraw(self, sum_of_withdrawal):
        sum_of_withdrawal = float(sum_of_withdrawal) - commission(sum_of_withdrawal)
        time_of_withdrawal = time.monotonic()
        self.transactions.append(f'withdrawal of {sum_of_withdrawal} made at {time_of_withdrawal}')
        self._balance -= sum_of_withdrawal


Account = BankAccount('w')
print(vars(Account))
Account.make_depo(10.0)
print(Account.balance)
