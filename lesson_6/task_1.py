# 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
#
#    Input:
#
# coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
# code = ('BTC', 'ETH', 'XRP', 'LTC')
#
#    Output:
#
# {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def create_dict(*args: tuple) -> dict:
    new_dict = dict(zip(*args))
    return new_dict


keys = tuple([key for key, value in create_dict(coin, code).items()])
values = tuple([value for key, value in create_dict(coin, code).items()])
