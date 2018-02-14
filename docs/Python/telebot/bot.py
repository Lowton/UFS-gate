import telebot
import check, config
import time, logging

logger = logging.getLogger('Telebot')
logger.setLevel(logging.DEBUG)

fl = logging.FileHandler('Telebot-debug.log')
fl.setLevel(logging.DEBUG)

cl = logging.StreamHandler()
cl.setLevel(logging.INFO)

flformatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
clformatter = logging.Formatter('%(asctime)s: %(message)s')
fl.setFormatter(flformatter)
cl.setFormatter(clformatter)

logger.addHandler(fl)
logger.addHandler(cl)

slave = telebot.TeleBot(config.token)
adm_chat_id = '78193601'


slave.send_message(adm_chat_id,'Я запустился!')
logger.debug('Отправлено сообщение "Я запустился!"')
com = 'Получена комманда {}.'
docids = []

logger.info('Запущен бот')

# Форматируем сообщение
def msg_format(msg):
    msg = str(msg)
    inj = ""
    text = ""
    msg = msg.replace(', ',',')
    msg = msg.replace(': {', ':\n   {')
    msg = msg.replace('},','},\n')
    msg = msg.replace(',',',\n')
    return msg

@slave.message_handler(commands=['check'])
def command_check(msg):
    #Получаем список строк для вывода
    docs = check.check_doc()
    logger.info(com.format('check'))
    if not docs:
        slave.send_message(msg.chat.id, 'Нет подозрительных.')
        logger.debug('Отправлено сообщение "Нет подозрительных."')
        return
    nothing_new = False
    for item in docs:
        if docids.count(item[0]) == 0:
            slave.send_message(msg.chat.id, item[1])
            logger.debug('Отправлено сообщение "{}"'.format(item[1]))
            docids.append(item[0])            
        else:
            if not nothing_new:
                slave.send_message(msg.chat.id, 'Ничего нового.')
                logger.debug('Отправлено сообщение "Ничего нового."')
            nothing_new = True

@slave.message_handler(commands=['reset'])
def command_reset(msg):
    logger.info(com.format('reset'))
    for item in docids:
        slave.send_message(msg.chat.id,
                           'Сброшен документ с id {}'.format(item))
        logger.debug('Отправлено сообщение "Сброшен документ с id {}"'.format(item))
        

@slave.message_handler(commands=['test'])
def test_command(msg):
    logger.info(com.format('test'))
    slave.send_message(msg.chat.id,
                       'Ты чё ввёл команду "ТЕСТ"??\n{}'.format(str(msg.chat.id)))
    logger.debug('Отправлено сообщение "Ты чё ввёл команду "ТЕСТ"?? {}"'.format(str(msg.chat.id)))

@slave.message_handler(commands=['exit'])
def command_exit(msg):
    slave.send_message(msg.chat.id, 'Отключаюсь.')
    logger.debug('Отправлено сообщение "Отключаюсь."')
    logger.info('Отключение бота')
    exit()

@slave.message_handler(commands=['129'])
def command_129(msg):
    slave.send_chat_action(msg.chat.id, 'find_location')
    slave.send_venue(msg.chat.id
                     ,53.5104636050214, 49.2724300231295
                     ,'Magikarp', 'С 44 по 59 минут.'
                     ,foursquare_id = '#129')
#                     ,reply_to_message_id = msg.message_id)


@slave.message_handler(func=lambda message: True, content_types=["text"])
def repeat_all_mess(msg):
    if config.debug: slave.send_message(msg.chat.id, str(msg))
    else: slave.send_message(msg.chat.id, msg.text)
    logger.info('Переотправлено сообщение "{}"'.format(msg.text))

@slave.message_handler(func=lambda message: True, content_types=['audio',
                                                                 'document',
                                                                 'photo',
                                                                 'sticker',
                                                                 'video',
                                                                 'voice',
                                                                 'contact',
                                                                 'location',
                                                                 'venue',
                                                                 'new_chat_member',
                                                                 'left_chat_member'])
def repeat_all_mess(msg):
    slave.send_message(msg.chat.id,
                       "Тип сообщения: " + str(msg.content_type),
                       reply_to_message_id = msg.message_id)
    logger.info('Переотправлено сообщение типа "{}"'.format(str(msg.content_type)))    
    if config.debug: slave.send_message(msg.chat.id, msg_format(msg))
        

if __name__ == '__main__':
    slave.polling(none_stop = True)
    while True:
        docs = check.check_doc()
        for item in docs: slave.send_message(adm_chat_id, item[1])
        slave.send_message(adm_chat_id, "Пробежала тестовая кукарача!")
        logger.info('30 sec remain')
        time.sleep(30)
