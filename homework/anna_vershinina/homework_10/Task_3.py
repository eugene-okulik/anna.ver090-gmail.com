PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

""" Initial solution
lines = PRICE_LIST.splitlines()
print(lines)

items = [line.split() for line in lines]
print(items)

dict_1 = dict(items)
print(dict_1)
"""

new_dict = {
    key: int(value[:-1]) for key, value in (
        line.split() for line in PRICE_LIST.splitlines()
    )
}
print(new_dict)
