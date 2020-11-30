import telebot
from telebot import types
from namaz_time import concat_nt
import datetime 
from api import API



abot = telebot.TeleBot(API)


@abot.message_handler(commands=['start'])
def send_message(message):
    abot.send_message(message.chat.id, 'введите /time для получения корректного времени намаза')


@abot.message_handler(commands=['time'])
def send_message(message):
    ac = datetime.datetime.today().strftime('%B %d\n%H:%M')
    # for k, v in concat_nt().items():
    abot.reply_to(message, str(concat_nt()).
    replace(',','\n\n').replace('{', '').replace('}', '').replace("'", '').upper(), 
    parse_mode="Markdown")

    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_time = types.KeyboardButton('/time')
    markup_reply.add(sub_time)
    abot.send_message(message.chat.id, ac, reply_markup=markup_reply)



if __name__ == "__main__":
    abot.polling()
