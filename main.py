from config import BOT
from telebot import types
from buttons import get_main_keyboard
from lifePrediction import birth_year_woman_energy, birth_year_men_energy
from moneyPrediction import birth_date_money


@BOT.message_handler(commands=['start'])
def main(message):
    BOT.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>, рады тебя видеть!',
                     reply_markup=get_main_keyboard(),
                     parse_mode='html'
                     )


@BOT.message_handler(func=lambda message: message.text == 'Cделать прогноз')
def answer_prediction(message):
    markup = types.InlineKeyboardMarkup()
    money_btn = types.InlineKeyboardButton('Прогноз на деньги', callback_data='money')
    life_btn = types.InlineKeyboardButton('Прогноз на энергию', callback_data='life')
    markup.row(money_btn)
    markup.row(life_btn)
    BOT.send_message(message.chat.id, f'Какой именно прогноз вас интересует?', reply_markup=markup)


@BOT.message_handler(func=lambda message: message.text == 'Mагазин товаров')
def shop_fnc(message):
    BOT.send_message(message.chat.id,
                     f'На текущий момент вы можете ознакомиться с нашими товарами по ссылке '
                     f'https://prana-shop.ru/magic-candles')


@BOT.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'money':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        sent_prediction = types.InlineKeyboardButton('Назад', callback_data='sent_prediction')
        markup.row(sent_prediction)
        BOT.send_message(callback.message.chat.id, 'Eсли у Вас никак не складываются дела с деньгами сегодня, то самое '
                                                   'время узнать, почему именно, так происходит? Учесть ошибки, взять '
                                                   'всё самое лучшее и следовать тем рекомендациям, которые изложены '
                                                   'далее. И у Вас, непременно, всё будет хорошо! \n '
                                                   '<b>Для этого введите свою дату рождения в формате ДД.ММ</b>',
                         parse_mode='html', reply_markup=markup)
        BOT.register_next_step_handler(callback.message, birth_date_money)
    elif callback.data == 'back_sex':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        women_btn_life = types.InlineKeyboardButton('Женский', callback_data='women_life')
        men_btn_life = types.InlineKeyboardButton('Мужской', callback_data='men_life')
        sent_prediction = types.InlineKeyboardButton('Назад', callback_data='sent_prediction')
        markup.add(women_btn_life, men_btn_life)
        markup.row(sent_prediction)
        BOT.send_message(callback.message.chat.id, 'Выберете ваш пол', reply_markup=markup)
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
    elif callback.data == 'life':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        women_btn_life = types.InlineKeyboardButton('Женский', callback_data='women_life')
        men_btn_life = types.InlineKeyboardButton('Мужской', callback_data='men_life')
        sent_prediction = types.InlineKeyboardButton('Назад', callback_data='sent_prediction')
        markup.add(women_btn_life, men_btn_life)
        markup.row(sent_prediction)
        BOT.send_message(callback.message.chat.id, 'Выберете ваш пол', reply_markup=markup)
    elif callback.data == 'women_life':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        back_sex = types.InlineKeyboardButton('Назад', callback_data='back_sex')
        markup.row(back_sex)
        BOT.send_message(callback.message.chat.id, 'Введите ваш год рождения в формате ГГГГ', reply_markup=markup)
        BOT.register_next_step_handler(callback.message, birth_year_woman_energy)
    elif callback.data == 'men_life':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        back_sex = types.InlineKeyboardButton('Назад', callback_data='back_sex')
        markup.row(back_sex)
        BOT.send_message(callback.message.chat.id, 'Введите ваш год рождения в формате ГГГГ', reply_markup=markup)
        BOT.register_next_step_handler(callback.message, birth_year_men_energy)
    elif callback.data == 'sent_prediction':
        BOT.clear_step_handler_by_chat_id(callback.message.chat.id)
        return answer_prediction(callback.message)


BOT.polling(non_stop=True)
