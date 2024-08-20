from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Cделать прогноз'),
                 KeyboardButton('Mагазин товаров'))
    return keyboard
