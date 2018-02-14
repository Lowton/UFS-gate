import config, sqlite
import random
import datetime
from log import log

newpokemon = False

while newpokemon == False:
    #Запуск рандомизатора
    randrank = random.randrange(config.limit)
    #запускаем функцию формирования списка покемонов
    pokelist = sqlite.__search(randrank)
    # выбираем из списка одного покемона
    randpok = pokelist[random.randrange(int(len(pokelist)))] 
    log.info('Выпавшее число: ' + str(randrank) + '; Выбранный покемон: ' + str(randpok[0]) + ' ' + randpok[1]) 

    recentlist = sqlite.__last((datetime.datetime.now()-datetime.timedelta(days=config.datedelta)).strftime('%Y-%m-%d'))

    if recentlist.count(str(randpok[0])):
        log.info(randpok[1] + ' был в течение предыдущих ' + str(config.datedelta) + ' дней')
        continue
    else:
        #log.debug(randpok[3])
        endDate = (datetime.datetime.now() + datetime.timedelta(days=randpok[3])).strftime('%Y-%m-%d')
        #log.debug(endDate)
        sqlite.__log(randpok[0],
                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                     endDate)
        print('До ' + endDate + ' ищем покемона: ' + randpok[1])
        log.info('Покемон ' + randpok[1] + '; до ' + endDate)
        newpokemon = True
