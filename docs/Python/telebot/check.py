##########################################################
# Скрипт проверки подозрительных документов
# Версия 2
# Кузьменко Алексей
# РТС-Банк
##########################################################

import pyodbc # Грузим модуль для работы с ODBC
import datetime
import config

def check_doc():
    table = []
    conn = pyodbc.connect(config.ibank_connect)
    # Рисуем образец сообщения
    message = 'Документ №{0} клиента {1} от {2} помечен подозрительным {3} в {4}.'

    # Делаем запрос платёжке со статусом подозрительный (12)
    doc = conn.cursor()
    doc.execute("""SELECT payer_name,date_doc,act_time,num_doc,doc_id
                   FROM ibank2.ibank2.payment
                   where status_doc=12""")
    doc = doc.fetchall()
    # Для каждой строки в полученной таблице повторяем
    for row in doc:
        docname = row[0]
        docdate = row[1].strftime("%d.%m.%y")
        actdate = row[2].strftime("%d.%m.%y")
        acttime = row[2].strftime("%H:%M:%S")
        docnum = row[3]
        docid = row[4]
        # заполняем образец сообщения
        table.append([docid, message.format(docnum,docname,docdate,actdate,acttime)])
    return(table)
