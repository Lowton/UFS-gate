import sqlite3
import config
from log import log


def __addRank(rank,value):
    dbconn = sqlite3.connect(config.db)
    dbconn.execute('insert into ranks values (?,?)', (rank,value))
    dbconn.commit()
    dbconn.close()

# Функция определения списка покемонов по выборке из таблицы
def __search(value):
    t = (value,)
    rank = 0
    dbconn = sqlite3.connect(config.db)
    cur = dbconn.cursor()
    cur.execute('select * from ranks where id=?', t)
    rank = cur.fetchone()[1]
    log.info('[SQL] Категория редкости покемона: ' + str(rank))
    cur.execute('select * from pokemon where rank=?', (rank,))
    table = cur.fetchall()
    return table

def __test(value):
    t = (value,)
    rank = 0
    dbconn = sqlite3.connect(config.db)
    cur = dbconn.cursor()
    cur.execute('select * from pokemon where id=?', t)
    print(cur.fetchone())
    if cur.fetchone(): rank = cur.fetchone()[1]
    dbconn.close()
    return rank

# Функция журналирования появившихс япокемонов
def __log(value,date,duration):
    dbconn = sqlite3.connect(config.db)
    dbconn.execute('insert into logger values (?,?,?)', (value,date,duration))
    dbconn.commit()
    dbconn.close()

# Функция выдачи списка последних покемонов
def __last(date):
    dbconn = sqlite3.connect(config.db)
    loglist = []
    cur = dbconn.cursor()
    cur.execute('select pokemon from logger where StartDate > ?', (date,))
    for row in cur.fetchall(): # обрабатываем построчно результат
        loglist.append(row[0])
    dbconn.close()
    return loglist
