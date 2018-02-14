import pyodbc
import config
from log import log

# Ищет записи в таблице сессий, если находит, то возвращает массив с ИНН
def __search_dublicate(inn,date):
    result_list = []
    conn=pyodbc.connect(config.db_connect)
    duble = conn.cursor()
    duble.execute("""SELECT Name,INN,IP,Date,Phone
                     FROM ibank_delta.dbo.Sessions
                     where inn = '{inn}'
                       and date = '{date}'""".format(inn=inn, date=date))
    for row in duble.fetchall():
        result_list.append(row[1])
    conn.close()
    log.info(result_list)
    return result_list
                  
def __insert(name, inn, ip, date, phone):
    conn = pyodbc.connect(config.db_connect)
    values = (name, inn, ip, date, phone)
    log.info(values)    
    conn.execute('insert into ibank_delta.dbo.Sessions values (?,?,?,?,?)', values)
    conn.commit()
    conn.close()

def __get_max_date():
    conn = pyodbc.connect(config.db_connect)
    ld = conn.cursor()
    ld.execute('SELECT max(Date) FROM Sessions')
    last_date = ld.fetchone()
    log.info(last_date)
    return last_date[0].strftime("%Y-%m-%d")

def __select():
    conn = pyodbc.connect(config.work_connect)
    session = conn.cursor()
    last_date = __get_max_date()
    log.info(last_date)
    session.execute("""SELECT cl.name_cln,cl.inn_cln,lt.address,lt.act_time,cl.phone_cln_sms
                   FROM ibank2.ibank2.login_time lt left join ibank2.ibank2.clients cl
                     on lt.client_id = cl.client_id
                   where lt.act_time > '{}'
                   ORDER BY lt.act_time""".format(last_date))

    for row in session.fetchall():
        name = row[0]
        inn = row[1]
        ip = row[2]
        date = row[3].strftime("%Y-%m-%d %H:%M:%S")
        phone = row[4]
        log.info(row)
        if __search_dublicate(inn,date).count(str(inn)):
            log.info('Есть такое значение')
        else:
            if name:
                log.info('Значение записано')
                __insert(name, inn, ip, date, phone)
                print("Дата: {1}; контора: {0}.".format(name,date))
            else:
                log.info('Нулевое значение имени')
    conn.close()
    

