import os
import pip

pip.main(['install', 'pytelegrambotapi'])
import telebot
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import time

bot = telebot.TeleBot('5728913288:AAGH4d7JWq36BxGvwtpnuH8N2-3U4VLHrw8')
owm = OWM('7ed24f7d519bd0b48d804372aa754775')
mgr = owm.weather_manager()
answer = ''

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        s_sky = w.detailed_status  # 'clouds'

        s_wind = w.wind()
        w.humidity  # 87
        s_temper = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

        w.rain  # {}
        w.heat_index  # None
        w.clouds  # 75

        wind = s_wind["speed"]
        temper = round(s_temper["temp"])

        answer = "Температура: " + str(temper) + ", на небе: " + str(s_sky) + ", ветер: " + str(wind) + "м/с"

        bot.send_message(message.chat.id, answer)
        print(message.text)
        print(answer)
    except:
        error = "Не могу прочитать, здесь что то на эльфийском."
        bot.send_message(message.chat.id, error)
        print(message.text)

bot.polling(non_stop=True, interval=0)
