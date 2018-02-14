import config, pomolog, pomodb # настройки
import tkinter


def __log(level, msg):
    if   level == 0: pomolog.log.critical(msg)
    elif level == 1: pomolog.log.error(msg)
    elif level == 2: pomolog.log.warn(msg)
    elif level == 3: pomolog.log.info(msg)
    elif level == 4: pomolog.log.debug(msg)
    else print('Да ты угараешь! Уровень от 0 до 4, другие варианты от лукавого!')


# Настройка ГУИ
root = tkinter.Tk()

