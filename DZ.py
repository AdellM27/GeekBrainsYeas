# Задание 1

Element_tip = ['drtgg', 1, (2, 1), [1, 2], 3.1, True, frozenset('1'), set('1')]

for el in Element_tip:
    print(type(el))

# Задание 3
new_dict = {"1": "zima", "2": "vesna", "3": "leto", "4": "osen"}
new_list1 = ["zima", "vesna", "leto", "osen"]

use = int(input("Введите месяц"))

if use == 1 or use == 2 or use == 12:
    print(new_list1[0])
elif use == 3 or use == 4 or use == 5:
    print(new_list1[1])
elif use == 6 or use == 7 or use == 8:
    print(new_list1[2])
elif use == 9 or use == 10 or use == 11:
    print(new_list1[3])
elif use > 12:
    print("Ошибка")

# Задание 4

strin = input("введите предложение ")
worl = []
number = 1

for element in range(strin.count(' ') + 1):
    worl = strin.split()
    if len(str(worl)) <= 10:
        print(f" {number} {worl[element]}")
        number += 1
    else:
        print(f" {number} {worl[element][0:10]}")
        number += 1

# Задание 5

my_list = [7, 5, 3, 3, 2]
use = int(input("введите число"))

for el in range(len(my_list)):
    if my_list[el] == use:
        my_list.insert(el + 1, use)
        break
    elif my_list[0] < use:
        my_list.insert(0, use)
    elif my_list[-1] > use:
        my_list.append(use)
    elif my_list[el] > use and my_list[el + 1] < use:
        my_list.insert(el + 1, use)
print(my_list)

# Задание 6

products = []

n = int(input("введите число товаров"))

for i in range(1, n + 1):
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')

    params = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }

    products.append((i, params))

print(products)


products1 = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

analitics = {}

for i, product in products1:
    for k, v in product.items():
        if analitics.get(k) == None:
            analitics[k] = []
        analitics[k].append(v)

for k in analitics.keys():
    analitics[k] = list(set(analitics[k]))

print(analitics)


