from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)

# Подрубаем протоколирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Создаём апдейтер с токеном бота
updater = Updater(token='284465130:AAGil5Wf-16wHooCJkrLhPtvMHDk9mEqPB0')

#для быстрого доступа к диспатчеру можно его инициализировать ручками
dispatcher = updater.dispatcher

# Функция при старте
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Я бот-хуебот пошли мне команду /off и я выключусь!")

# Задаём хендлер для команды start
start_handler = CommandHandler('start', start)
# Регистрируем хендлер в диспатчере
dispatcher.add_handler(start_handler)

def off(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Выключаюсь…")
    updater.stop()

#Задаём хендлер для отключения
off_handler = CommandHandler('off', off)
dispatcher.add_handler(off_handler)

# Функция эхо-отклика
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# Задаём хендлер для текстовых сообщений
echo_handler = MessageHandler(Filters.text, echo)
# регистрируем в диспатчере
dispatcher.add_handler(echo_handler)

# функция капитализации сообщения
def caps(bot, update, args):
    #Капитализируем аргумент команды
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

# Задаём хендлер для команды caps с наличием аргументов и регистрируем его
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                         text="Слышь! Я не понимаю чё ты хочешь от меня!")

# Задаём хендлер для всех остальных команд (заглушку)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#Запускаем бота
updater.start_polling()
