from buttons import get_main_keyboard
from config import BOT
from telebot import types


def birth_year_woman_energy(message):
    year = message.text
    if len(year) == 4 and (int(year) % 2 == 0):
        markup = types.InlineKeyboardMarkup()
        sent_prediction = types.InlineKeyboardButton('Сделать еще одно предсказание',
                                                     callback_data='sent_prediction')
        markup.row(sent_prediction)
        BOT.send_message(message.chat.id, f'Девушка с энергией Ян.Девочка-мальчик с сильным характером. '
                                          f'Всегда всё делает сама, отказывается от помощи что-то доказывает'
                                          f'Фраза: “Я сама”.'
                                          f'Задача: Прокачать женскую энергию. Если этим не заниматься, то'
                                          f' начинает грубеть голос, начинаются проблемы по женски, обволосинение, '
                                          f'выработка тестостерона. Часто остаются одинокими.Девушки Ян притягивают '
                                          f'Мужчин Инь, но пожив вместе она понимает, что это не то.'
                                          f'В этом случае она будет главная в отношениях, будет тянуть семью на себе. '
                                          f'Интимных отношений не будет.', reply_markup=markup)
    elif len(year) == 4 and (int(year) % 2 != 0):
        markup = types.InlineKeyboardMarkup()
        sent_prediction = types.InlineKeyboardButton('Сделать еще одно предсказание',
                                                     callback_data='sent_prediction')
        markup.row(sent_prediction)
        BOT.send_message(message.chat.id, f'Девушка с энергией Инь.'
                                          f'Девочка-девочка. Она мягкая, женственная и уступчивая, '
                                          f'занимается домашним хозяйством, готовкой.Фраза: “Лишь бы милый был рядом '
                                          f'и ничего мне не надо”', reply_markup=markup)
    elif len(year) != 4:
        markup = types.InlineKeyboardMarkup()
        back_year_money_prediction = types.InlineKeyboardButton('Назад', callback_data='back_sex')
        markup.row(back_year_money_prediction)
        BOT.send_message(message.chat.id, f'Введен неверный формат года рождения',
                         reply_markup=markup)
    elif year == 'Mагазин товаров':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        BOT.send_message(message.chat.id, f'На текущий момент вы можете ознакомиться с нашими товарами по ссылке '
                                          f'https://prana-shop.ru/magic-candles')
    elif year == '/start':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        BOT.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>, рады тебя видеть!',
                         reply_markup=get_main_keyboard(),
                         parse_mode='html'
                         )
    elif year == 'Cделать прогноз':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        markup = types.InlineKeyboardMarkup()
        money_btn = types.InlineKeyboardButton('Прогноз на деньги', callback_data='money')
        life_btn = types.InlineKeyboardButton('Прогноз на энергию', callback_data='life')
        markup.row(money_btn)
        markup.row(life_btn)
        BOT.send_message(message.chat.id, f'Какой именно прогноз вас интересует?', reply_markup=markup)
    else:
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        markup = types.InlineKeyboardMarkup()
        back_year_money_prediction = types.InlineKeyboardButton('Назад', callback_data='back_sex')
        markup.row(back_year_money_prediction)
        BOT.send_message(message.chat.id, f'Введен неверный формат года рождения',
                         reply_markup=markup)
        BOT.register_next_step_handler(message, birth_year_woman_energy)


def birth_year_men_energy(message):
    year = message.text
    if len(year) == 4 and (int(year) % 2 == 0):
        markup = types.InlineKeyboardMarkup()
        sent_prediction = types.InlineKeyboardButton('Сделать еще одно предсказание',
                                                     callback_data='sent_prediction')
        markup.row(sent_prediction)
        BOT.send_message(message.chat.id, f'Мужчина с энергией Ян.Самостоятельный мужчина, он берёт на себя '
                                          f'ответственность за себя и партнера.Способен проблемы семьи '
                                          f'переложить на себя.Часто мало озабочен своим внешним видом',
                         reply_markup=markup)
    elif len(year) == 4 and (int(year) % 2 != 0):
        markup = types.InlineKeyboardMarkup()
        sent_prediction = types.InlineKeyboardButton('Сделать еще одно предсказание',
                                                     callback_data='sent_prediction')
        markup.row(sent_prediction)
        BOT.send_message(message.chat.id, f'Мужчина с энергией Инь.Чувствителен и сентиментален.Не берет '
                                          f'ответственность за партнера и перекладывает ответственность на женщину.'
                                          f'Фраза: “Ну я же сделал, как ты хотела” Эти мужчины истерички, '
                                          f'сплетницы, любят спорить. Щепетильно относятся к внешнему виду.'
                                          f'Фраза: “Сколько могу, столько и зарабатываю”.'
                                          f'Не пойдет на вторую работу.', reply_markup=markup)
    elif year == 'Mагазин товаров':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        BOT.send_message(message.chat.id, f'На текущий момент вы можете ознакомиться с нашими товарами по ссылке '
                                          f'https://prana-shop.ru/magic-candles')
    elif year == '/start':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        BOT.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>, рады тебя видеть!',
                         reply_markup=get_main_keyboard(),
                         parse_mode='html'
                         )
    elif year == 'Cделать прогноз':
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        markup = types.InlineKeyboardMarkup()
        money_btn = types.InlineKeyboardButton('Прогноз на деньги', callback_data='money')
        life_btn = types.InlineKeyboardButton('Прогноз на энергию', callback_data='life')
        markup.row(money_btn)
        markup.row(life_btn)
        BOT.send_message(message.chat.id, f'Какой именно прогноз вас интересует?', reply_markup=markup)
    else:
        BOT.clear_step_handler_by_chat_id(message.chat.id)
        BOT.send_message(message.chat.id, f'Введен неверный формат года рождения')
        BOT.register_next_step_handler(message, birth_year_men_energy)
