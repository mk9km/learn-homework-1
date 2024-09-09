"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

STOP_WORD = 'хорошо'


def hello_user():
    """
    Замените pass на ваш код
    """
    user_input = ''
    print('-' * 20)
    print(f'Hint: press CTRL + Z/X/C/F2 for interruption')
    print('-' * 20)
    while user_input != STOP_WORD:
        print(' - Как дела?')
        try:
            user_input = input()
        except KeyboardInterrupt:
            break
        user_input = user_input.lower()
        user_input = user_input.strip()
        print('-' * 20)
    print(' - Пока!')

if __name__ == "__main__":
    hello_user()
