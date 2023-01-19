import telebot
from config import TOKEN, currencies
from extensions import APIException, CurrenciesPrise


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = """Для работы бота введите следующие параметры через пробел: 
    <имя валюты> <имя валюты, в которую нужно перевести> <количество валюты>. 
    Названия валют вводите в единственном числе именительного падежа.
    Количество валюты в дробных числах вводите через точку (_._).
    Например, команда "евро рубль 100.50" рассчитает стоимость 100,50 евро в рублях.\n
    Доступные команды для бота: 
    /start, /help - вывод подсказки по работе бота,
    /values - список доступных валют"""
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}!\n" + text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = """Для работы бота введите следующие параметры через пробел: 
    <имя валюты> <имя валюты, в которую нужно перевести> <количество валюты>. 
    Названия валют вводите в единственном числе именительного падежа.
    Количество валюты в дробных числах вводите через точку (_._).
    Например, команда "евро рубль 100.50" рассчитает стоимость 100,50 евро в рублях.\n
    Доступные команды для бота: 
    /start, /help - вывод подсказки по работе бота,
    /values - список доступных валют"""
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:\n" + "\n".join(currencies.keys())
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) > 3:
            raise APIException("Слишком много параметров. \n(для вызова подсказки введите /help)")
        if len(values) < 3:
            raise APIException("Недостаточно данных. Необходимо ввести три параметра."
                                      "\n(для вызова подсказки введите /help)")
        quote, base, amount = values
        cost = CurrenciesPrise.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя. \n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду. \n {e}")
    else:
        text = f"Перевожу {quote.lower()}({currencies[quote.lower()]}) в {base.lower()}({currencies[base.lower()]}):\n" \
               f"Стоимость {amount} {currencies[quote.lower()]} составляет {round(cost, 2)} {currencies[base.lower()]}."
        bot.send_message(message.chat.id, text)


bot.polling()
