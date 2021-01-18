from lesson_6 import task_1
import unittest


class TestNewDict(unittest.TestCase):
    def test_keys(self):
        keys = tuple([key for key, value in task_1.create_dict(task_1.coin, task_1.code).items()])
        self.assertTupleEqual(task_1.coin, keys, 'keys are equal')

    def test_values(self):
        values = tuple([value for key, value in task_1.create_dict(task_1.coin, task_1.code).items()])
        self.assertTupleEqual(task_1.code, values, 'values are equal')

if __name__ == '__main__':
    unittest.main()
# coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
# code = ('BTC', 'ETH', 'XRP', 'LTC')
# new_dict = dict(zip(coin, code))
#
#
# def test(new_dict):
#     keys = tuple([key for key, value in new_dict.items()])
#     values = tuple([value for key, value in new_dict.items()])
#     if coin == keys and code == values:
#         print('Ok')
#     else:
#         print('Not ok!')
#
#
# test(new_dict)