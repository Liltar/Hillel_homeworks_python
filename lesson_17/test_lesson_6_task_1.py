coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
new_dict = dict(zip(coin, code))


def test(new_dict):
    keys = tuple([key for key, value in new_dict.items()])
    values = tuple([value for key, value in new_dict.items()])
    if coin == keys and code == values:
        print('Ok')
    else:
        print('Not ok!')


test(new_dict)
x`