"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

STOP_WORD = 'exit'
HELP_WORD = 'help'

questions_and_answers = {
    'как дела?': 'хорошо!',
    'что делаешь?': 'программирую.',
    'как тебя зовут?': 'меня зовут python.',
    'какоe у тебя хобби?': 'моё хобби - майнинг.',
    'ты любишь путешествовать?': 'да, очень люблю!.',
    'какая у тебя любимая еда?': 'моя любимая еда - гигабайты и флопсы.',
    'ты занимаешься спортом?': 'да, я занимаюсь киберспортом.',
    'как прошли твои выходные?': 'мои выходные были спокойными.',
    'какая у тебя любимая книга?': 'моя любимая книга - документация к python.'
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    print('-' * 20)
    print(f'Hint: enter {STOP_WORD} for exit')
    print(f'Hint: enter {HELP_WORD} for help')
    print('-' * 20)

    while True:
        print('Enter your question or command:')
        user_input = input()
        user_input = user_input.lower()
        user_input = user_input.strip()

        if user_input == STOP_WORD:
            print(' - Bye')
            quit()
        elif user_input == HELP_WORD:
            print('Possible questions:')
            for question in answers_dict:
                print(f' - {question.capitalize()}')
        elif user_input in answers_dict:
            key = user_input
            answer = answers_dict.get(key)
            print(f' - {answer.capitalize()}')
        else:
            print('Unknown command, try again')
        print('-' * 20)

if __name__ == "__main__":
    ask_user(questions_and_answers)
