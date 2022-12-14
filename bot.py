import re
import time
from datetime import datetime

import telebot

from db_methods import set_user_id, get_user_id, get_values

# bot token
bot = telebot.TeleBot('5266363672:AAEyg1z8QrEwfS31bJUhGybWZs7zpveD7wY')


def start_bot():
    # start command listener
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        print("start listener")
        bot.send_message(message.chat.id,
                         'Добрый день ' + message.from_user.first_name + ", вы подписались на уведомления о поставках.\nЕсли какой-нибудь из заказов доставят, вам пришлют уведомление")
        user_id = message.from_user.id
        rows = get_user_id()
        if len(rows):
            for row in rows:
                if user_id != row[0]:
                    set_user_id(int(user_id))
        else:
            set_user_id(int(user_id))
        pass

    # mass mailing method
    def mass_message():
        while True:
            x = datetime.now().hour
            if int(x) == 8:
                dates = get_values()
                date_today = datetime.now().strftime("%d-%m-%Y")
                date_today = re.sub(r'-', ".", date_today)
                for row in dates:
                    if re.search(row[4], date_today):
                        ids = get_user_id()
                        for user_id in ids:
                            bot.send_message(user_id[0],
                                             'Заказ № ' + str(row[1]) + ' на сумму ' + str(
                                                 row[3]) + ' руб ' + ' доставлен')
                            print('mass message sent to all users')
            print('end mass message check')
            time.sleep(3600)
        pass

    # start bot
    if __name__ == '__main__':
        try:
            print('start bot')
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)
    mass_message()
    time.sleep(10)
