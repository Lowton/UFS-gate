import pyodbc
import config
from log import log
from file import create_report

# Ищет записи в таблице сессий, если находит, то возвращает массив с ИНН

def __report(inn, begin_date='2000-01-01', end_date='2099-12-31'):
    conn = pyodbc.connect(config.db_connect)
    session = conn.cursor()
    last_date = __get_max_date()
    log.info(last_date)
    session.execute("""SELECT * FROM [ibank_delta].[dbo].[Sessions]
                       where Date between '{begin_date}' and '{end_date}'
                       and INN = '{inn}'""".format(inn=inn,
                                                   begin_date=begin_date,
                                                   end_date=end_date))
    company = ''

    for row in session.fetchall():
        name = row[0]
        if company == '': company = name.replace('"',"''")
        inn = row[1]
        ip = row[2]
        date = row[3].strftime("%Y-%m-%d %H:%M:%S")
        phone = row[4]
        log.info(row)
        report_data = name + '\t' + inn + '\t' + ip + '\t' + date + '\t' + phone
        create_report(company, report_data)
    conn.close()
    

