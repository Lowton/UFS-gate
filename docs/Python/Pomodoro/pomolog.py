import config # настройки
import logging # Протоколирование

# Конфигурация протоколирования
log = logging.getLogger('pomodoro')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

fh = logging.FileHandler(config.logfile)
fh.setLevel(logging.DEBUG)

fformatter = logging.Formatter('%(asctime)s\t%(levelname)s: %(message)s')
cformatter = logging.Formatter('%(levelname)s: %(message)s')

ch.setFormatter(cformatter)
fh.setFormatter(fformatter)

log.addHandler(ch)
log.addHandler(fh)
