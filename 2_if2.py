"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""
from typing import Tuple, NoReturn, Any, Dict

LP_STRING_VALUE = 'learn'

import enum

class Result(enum.Enum):
    wrong_type = 0
    equal = 1
    first_longer = 2
    lp = 3
    other = None

def check_string(str1: Any, str2: Any) -> Result:
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return Result.wrong_type
    elif str1 == str2:
        return Result.equal
    elif str2 == LP_STRING_VALUE:
        return Result.lp
    elif len(str1) > len(str2):
        return Result.first_longer
    else:
        return Result.other


def to_dict(var: Any) -> Dict:
    return {
        'value': var,
        'type': type(var),
        'length': len(var) if '__len__' in dir(var) else None
    }


def test(str1: Any, str2: Any) -> NoReturn:
    rv = check_string(str1, str2)
    print(
        '1st parameter: {0}'.format(to_dict(str1))
    )
    print(
        '2nd parameter: {0}'.format(to_dict(str2))
    )
    print(f'Result: {rv} - {rv.value}')
    print(f'-'*20)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    test(1111, '1111')
    test('1111', 1111)
    test('1111', '1111')
    test('w1w1w1w', 'e2e2e')
    test('w1w1w1w', 'learn')
    test('r3', 'learn')
    test('learn', 'r3')
    test('learn', 'w1w1w1w')
    test('e2e2e', 'w1w1w1w')

if __name__ == "__main__":
    main()
