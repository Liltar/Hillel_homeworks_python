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
import uuid
import time

# какой функцией указать время события так, чтобы оно не сдвигалось каждый раз?
# почему не прибавляет к балансу депозит?


class BankAccount():
    def __init__(self, name, unique_id, balance, transactions):
        self.name = name
        self.unique_id = uuid.uuid1(unique_id)
        self.balance = 0.0
        self.transactions = []

    def make_depo(self, sum_of_depo):
        sum_of_depo = float(sum_of_depo)
        time_of_depo = time.monotonic()
        self.transactions.append(f'deposit of {sum_of_depo} made at {time_of_depo}')
        return self.balance + sum_of_depo

    def withdraw(self, sum_of_withdrawal):
        sum_of_withdrawal = float(sum_of_withdrawal)
        time_of_withdrawal = time.monotonic()
        self.transactions.append(f'deposit of {sum_of_withdrawal} made at {time_of_withdrawal}')
        return self.balance - sum_of_withdrawal

    def get_balance(self):
        return self.balance


Account = BankAccount('w', 4, 5.0, [])
print(vars(Account))
Account.make_depo(10.0)
print(vars(Account))
print()