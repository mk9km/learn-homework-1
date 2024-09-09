"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
import enum

from typing import NoReturn

MAX_LIVING_AGE_YEARS = 120

class Activity(enum.Enum):
    kindergarten = 'kindergarten'
    school = 'school'
    university = 'university'
    work = 'work'
    pension = 'pension'


def get_activity(age: int) -> Activity:
    """
    Get activity by age
    """
    if not isinstance(age, int) or age < 0 or age > MAX_LIVING_AGE_YEARS:
        raise Exception(f'Incorrect age: {age}: should be integer and more than 0 and less than {MAX_LIVING_AGE_YEARS}')

    if age < 7:
        return Activity.kindergarten
    elif age < 18:
        return Activity.school
    elif age < 25:
        return Activity.university
    elif age < 65:
        return Activity.work
    else:
        return Activity.pension


def input_age() -> int:
    print(
        f"For determining a user’s activity, input the user’s age "
        f"(integer more than or equal to 0 and less than or equal to {MAX_LIVING_AGE_YEARS}):"
    )
    user_input = input()
    return int(user_input) # No type cast exception handling: assumes, that user can read the message above


def output_activity(activity: Activity) -> NoReturn:
    print(f"User's activity is '{activity.value}'")


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = input_age()
    user_activity = get_activity(user_age)
    output_activity(user_activity)


if __name__ == "__main__":
    main()
