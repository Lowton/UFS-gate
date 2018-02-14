import config, mssql
from log import log

log.info('Скрипт запущен')

mssql.__select()

log.info('Скрипт закончен')
