"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
input_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

from typing import List, NoReturn, Dict


def avg(data: List) -> float:
    rv = sum(data) / len(data)
    return rv


def get_product_info(data: Dict) -> Dict:
    if not ('product' in data and 'items_sold' in data):
        raise Exception(f"Incorrect data format: expects 'product' and 'items_sold' keys")

    if not (isinstance(data.get('product'), str) and isinstance(data.get('items_sold'), list)):
        raise Exception(f"Incorrect data format: expects 'product' should be a string and 'items_sold' a list")

    if not data.get('product'):
        raise Exception(f"Incorrect data format: 'product' value cannot be empty")

    items = data.get('items_sold')

    rv = {
        'name': data.get('product'),
        'sum': sum(items) if items else 0,
        'avg': avg(items) if items else 0
    }

    return rv


def output_product_info(info: Dict) -> NoReturn:
    print(f"Name: {info.get('name')}")
    print(f"Sum: {info.get('sum')}")
    print(f"Avg: {info.get('avg')}")
    print('-'*20)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total = {'product': 'Total', 'items_sold': []}
    for data in input_data:
        total['items_sold'] += data['items_sold']

        product_info = get_product_info(data)
        output_product_info(product_info)

    total_info = get_product_info(total)
    output_product_info(total_info)


if __name__ == "__main__":
    main()
