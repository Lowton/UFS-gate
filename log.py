import logging # Протоколирование

# Конфигурация протоколирования
log = logging.getLogger('pomodoro')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler() # вывод на консоль
ch.setLevel(logging.ERROR)

fh = logging.FileHandler('pomo.log') # вывод в файл
fh.setLevel(logging.DEBUG)

fformatter = logging.Formatter('%(asctime)s\t%(levelname)s: %(message)s')
cformatter = logging.Formatter('%(levelname)s: %(message)s')

ch.setFormatter(cformatter)
fh.setFormatter(fformatter)

log.addHandler(ch)
log.addHandler(fh)

log.debug('%s message', 'debug')
log.info('info message')
log.warn('warn message')
log.error('error message')
log.critical('critical message')
