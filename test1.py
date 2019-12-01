inventory = {
    '1': 'телефон'
}
thing = "not"
i = 0


def inv():
    for key, value in inventory.items():
        print(key + ')', value)
    print('Что бы выбрать предмет нужно вести номер')
    thing = input('Выбрать: ')
    return thing

if __name__ == '__main__':
    inventory.setdefault('2', 'фонарик')
    inventory.setdefault('3', 'ключ')
    act = input('Что бы посмотреть инвентарь ведите i : ')
    if act == 'i':
        thing = inv()
    if thing == '1' and i == 0:
        print('Остался 1% заряда, вы решили позвонить')
        act = input('1) Маме 2) В милицию: ')
        print('Вы звоните, но телефон отключился после первого гудка')
        i += 1
    elif thing == '3':
        print('Дверь открылось')
    else:
        print("Что мне с этим делать?")
    print(thing)