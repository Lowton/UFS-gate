import logging # Протоколирование
import config

# Конфигурация протоколирования
log = logging.getLogger(config.loggerName)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler() # вывод на консоль
ch.setLevel(logging.ERROR)

fh = logging.FileHandler(config.logFile) # вывод в файл
fh.setLevel(logging.DEBUG)

fformatter = logging.Formatter('%(asctime)s\t%(levelname)s: %(message)s')
cformatter = logging.Formatter('%(levelname)s: %(message)s')

ch.setFormatter(cformatter)
fh.setFormatter(fformatter)

log.addHandler(ch)
log.addHandler(fh)

