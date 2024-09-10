"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from typing import Tuple

import ephem
import settings
from telegram.ext import Updater, CommandHandler

PLANETS = [
    'Jupiter', 'Mars', 'Mercury', 'Moon', 'Neptune', 'Pluto', 'Saturn', 'Sun', 'Uranus', 'Venus',
]

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(update, context):
    print('/start')
    update.message.reply_text('Hi!')
    update.message.reply_text('Run "/planet <Planet>" to get a current planet constellation')
    update.message.reply_text(f'Known planets: {PLANETS}')

def _get_planet_by_name(name: str) -> ephem.Planet:
    if name == 'Jupiter':
        planet = ephem.Jupiter()
    elif name == 'Mars':
        planet = ephem.Mars()
    elif name == 'Mercury':
        planet = ephem.Mercury()
    elif name == 'Moon':
        planet = ephem.Moon()
    elif name == 'Neptune':
        planet = ephem.Neptune()
    elif name == 'Pluto':
        planet = ephem.Pluto()
    elif name == 'Saturn':
        planet = ephem.Saturn()
    elif name == 'Sun':
        planet = ephem.Sun()
    elif name == 'Uranus':
        planet = ephem.Uranus()
    elif name == 'Venus':
        planet = ephem.Venus()
    else:
        raise Exception(f'Planet {name} is not in the list of known planets: {PLANETS}')
    planet.compute()
    return planet

def _get_constellation_by_planet(planet: ephem.Planet) -> Tuple[str, str]:
    return ephem.constellation(planet)

def get_planet(update, context):
    cmd, name = update.message.text.split()
    print(cmd, name)
    try:
        planet = _get_planet_by_name(name)
        constellation = _get_constellation_by_planet(planet)
        print(constellation)
        update.message.reply_text(constellation)
    except Exception as e:
        print(e)
        update.message.reply_text('Error')
        update.message.reply_text('Please check input command:')
        update.message.reply_text('Run "/planet <Planet>"')
        update.message.reply_text(f'Known planets: {PLANETS}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
