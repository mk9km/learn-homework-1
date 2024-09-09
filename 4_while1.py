"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""

STOP_WORD = 'хорошо'


def hello_user():
    """
    Замените pass на ваш код
    """
    user_input = ''
    print('-'*20)
    print(f'Hint: enter "{STOP_WORD}" for exit')
    print('-'*20)
    while user_input != STOP_WORD:
        print(' - Как дела?')
        user_input = input()
        user_input = user_input.lower()
        user_input = user_input.strip()
        print('-' * 20)
    print(' - Bye')

if __name__ == "__main__":
    hello_user()
