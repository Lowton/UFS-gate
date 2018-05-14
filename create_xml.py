from pyodbc import connect
from config import ubs_connect
from datetime import datetime
from log import log

# Определяем ID клиента по входящему параметру — ID договора ДБО
def get_client_id(contract_id):
    conn = connect(ubs_connect)
    cur = conn.cursor()
    cur.execute("""select id_client
                   from rb_contract
                   where id_contract = {}""".format(contract_id))
    client_id = cur.fetchone()[0]
    log.info('ID клиента ' + str(client_id))
    conn.close()
    return client_id

#
def get_id(table, value):
    request_id = "(select id_field from {table} \
             where name_field = '{value}')".format(table=table, value=value)
    log.info(request_id)    
    return request_id

# Определяем логин по ID договора
def get_login(contract_id):
    conn = connect(ubs_connect)
    cur = conn.cursor()
    cur.execute("""SELECT ra.login FROM RB_ABONENT ra
                   WHERE ra.ID_ABONENT = (
                         SELECT rca.ID_ABONENT FROM RB_CONTRACT_ABONENT rca
                         WHERE rca.ID_CONTRACT = {})""".format(contract_id))
    login = cur.fetchone()[0]
    log.info('Логин клиента: ' + login)
    conn.close()
    return login

# Определяем паспортные данные по ID клиента
def get_pasport(client_id):
    conn = connect(ubs_connect)
    cur = conn.cursor()
    cur.execute("""select document,reg_num,series_doc,reg_date,reg_organ
                   from clients
                   where id_client = {}""".format(client_id))
    pasport = cur.fetchone()
    conn.close()
    return pasport

# Делаем часть xml с информацией по паспортным данным
def create_pasport(client_id):
    pasport = get_pasport(client_id)
    document = 'Паспорт' if pasport[0] == 'Паспорт гражданина РФ' else Null
    serial = pasport[2]
    number = pasport[1]
    date = pasport[3].strftime("%Y-%m-%d")
    dept = pasport[4]
    log.info(document + '; ' + serial + '; ' + number + '; ' + date + '; ' + dept)
    xml = '<reg:identity-card series="{serial}" \
           number="{num}" issue-date="{date}" \
           issuer="{dept}" type="{doc}" />\
          '.format(serial=serial, num=number, date=date, dept=dept, doc=document)
    return xml

# Определяем адрес по ID клиента
def get_address(client_id):
    country_id = get_id('CLIENTS_ADDFL_DIC','Гражданство (подданство)')
    phone_id = get_id('RB_CONTRACT_ADDFL_DIC','Мобильный для ДБО')
    email_id = get_id('RB_CONTRACT_ADDFL_DIC','EMail клиента')
    
    conn = connect(ubs_connect)
    cur = conn.cursor()# Вот гавно какое! Вытащил страну из базы через доп.поля,
                       # а она не используется в xml’е (убрать если не пригодится)
    cur.execute("""select (select cas.FIELD FROM CLIENTS_ADDFL_STRING cas 
                           WHERE cas.ID_FIELD = {country_id} AND cas.ID_OBJECT = {client_id})
                          ,cca.post_index, cca.name_city
                          ,(cca.TYPE_STREET + '. ' + cca.NAME_STREET + ' '
                            + cca.NUM_BUILDING + '-' + cca.NUM_FLAT)
                          ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                            WHERE  rcas.ID_OBJECT = (SELECT rc.ID_CONTRACT FROM RB_CONTRACT rc
                                                     WHERE rc.ID_CLIENT = {client_id})
                            AND rcas.ID_FIELD = {phone_id})
                          ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                            WHERE  rcas.ID_OBJECT = (SELECT rc.ID_CONTRACT FROM RB_CONTRACT rc
                                                     WHERE rc.ID_CLIENT = {client_id})
                            AND rcas.ID_FIELD = {email_id})
                   from COM_CLIENTS_ADDRESS cca
                   where id_client = {client_id}""".format(country_id=country_id, client_id=client_id,
                                                           phone_id=phone_id,email_id=email_id))
    address = cur.fetchone()
    conn.close()
    return address

# Формируем часть xml с информацией об адресе.
def create_address(client_id):
    address = get_address(client_id)
    country = address[0]
    index = address[1]
    city = address[2]
    street = address[3]
    mail = address[5]
    phone = address[4] if address[4] else ''
    email = 'email="{}"'.format(mail) if mail else ''
    log.info('Адрес: ' + index + ', ' + country + ', ' + city + ', ' \
             + street + '. Т: ' + phone + ', @: ' + mail)
    xml = '''<reg:contacts address="{street}" zip-code="{index}" city="{city}"
             {email} phone="{phone}" />'''.format(street=street, index=index,
                                                  city=city, email=email,
                                                  phone=phone)
    return xml

# Определяем данные клиента по его ID
def get_person(client_id):
    conn = connect(ubs_connect)    
    cur = conn.cursor()
    cur.execute("""SELECT c.FIRST_NAME, c.MIDDLE_NAME,
                          c.LAST_NAME, c.INN, c.DATE_BIRTH
                   FROM CLIENTS c
                   WHERE c.ID_CLIENT = {}""".format(client_id))
    person = cur.fetchone()
    conn.close()
    return person

# Формируем xml с данными о клиенте
def create_person(client_id):
    person = get_person(client_id)
    
    first_name = person[0]
    middle_name = person[1]
    last_name = person[2]
    inn = person[3]
    birthday = person[4].strftime("%Y-%m-%d")
    log.info('Клиент: {0} {1} {2}; ИНН {3}; д.р. {4}.'.format(last_name, first_name,
                                                          middle_name,inn, birthday))
    xml = """<reg:person inn="{inn}" first-name="{first_name}"
              last-name="{last_name}" middle-name="{middle_name}"
              birthday="{birthday}">""".format(inn=inn, first_name=first_name,
                                               middle_name=middle_name,
                                               last_name=last_name,
                                               birthday=birthday) \
              + '\n' + create_pasport(client_id) \
              + '\n' + create_address(client_id) \
              + '\n</reg:person>'
    return xml

def get_contract(contract_id):
    phone_id = get_id('RB_CONTRACT_ADDFL_DIC','Мобильный для ДБО')
    
    conn = connect(ubs_connect)    
    cur = conn.cursor()
    cur.execute("""SELECT rc.NUM_CONTRACT, rc.DATE_BEGIN
                        ,(SELECT rcas.FIELD FROM RB_CONTRACT_ADDFL_STRING rcas
                          WHERE rcas.ID_OBJECT = {0} AND rcas.ID_FIELD = {1})
                   FROM RB_CONTRACT rc
                   WHERE ID_CONTRACT = {0}""".format(contract_id, phone_id))
    contract = cur.fetchone()
    conn.close()
    return contract

def create_contract(contract_id):
    contract = get_contract(contract_id)
    num = contract[0]
    open_date = contract[1].strftime("%Y-%m-%d")
    phone = contract[2] if contract[2] else ''
    log.info('Договор № {0} от {1} (т. {2})'.format(num, open_date, phone))
    xml = """<reg:contract doc-number="{num}" open-date="{date}"
              payment-activation="true" otp-phone="{phone}">
                <reg:bank bic="043678783" bic-type="ru" inn="6323066377"
                 account-number="30101810100000000783" name='АО "РТС-Банк"' />
                <reg:document-rights doc-type="free-document" create="true" sign-level="1" />
            </reg:contract>""".format(num=num, date=open_date, phone=phone)
    return xml

def get_accounts(contract_id):
    PS_id = get_id('CARD_PRODUCT_ADDFL_DIC','Код платежной системы')
    RBS_id = get_id('CARD_CONTRACT_ADDFL_DIC','RBSNumber')
    status_id = get_id('CARD_CONTRACT_ADDFL_DIC','Статус карты')

    conn = connect(ubs_connect)
    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT cp.num_card, cp.RBSNumber,
                                   cp.PS, cp.CARD_EXPIRE_DATE,
                                   cp.acc_main, cp.DATE_OPEN
                   from (
                         select cc.ID_ACCOUNT_MAIN, rc.ID_CONTRACT,
                                rp.ID_PRODUCT, cc.NUM_CARD,
                               (SELECT ccas.FIELD
                                FROM CARD_CONTRACT_ADDFL_STRING ccas
                                WHERE ccas.ID_FIELD = ({RBS_id})
                                AND ccas.ID_OBJECT = cc.ID_CONTRACT) RBSNumber,
                                cc.CARD_EXPIRE_DATE,
                               (SELECT cpa.FIELD_STRING
                                FROM CARD_PRODUCT_ADDFL cpa
                                WHERE cpa.ID_FIELD = ({PS_id})
                                AND cpa.ID_OBJECT = rp.ID_PRODUCT_EXT) PS,
                               (SELECT oa0.straccount
                                FROM od_accounts0 oa0
                                WHERE ID_ACCOUNT = cc.ID_ACCOUNT_MAIN) acc_main,
                                cc.DATE_OPEN,
                               (SELECT FIELD FROM CARD_CONTRACT_ADDFL_STRING
                                WHERE ID_FIELD = ({status_id})
                                AND ID_OBJECT = cc.ID_CONTRACT) StatusCard
                         from RB_CONTRACT rc, card_contract cc,
                              RB_MODEL_ADDFL_ARRAY rm, RB_PRODUCT rp
                         where rc.ID_CONTRACT = {contract_id}
                           and rc.ID_CLIENT = cc.ID_CLIENT_OWNER
                           and cc.DATE_CLOSE = '2222-01-01'
                           and rm.ID_OBJECT = 3
                           and rm.ID_FIELD =  7
                           and convert(int,rm.field_string) = rp.ID_PRODUCT
                           and cc.ID_PRODUCT = rp.ID_PRODUCT_EXT
                        ) cp left join RB_CONTRACT_ACC rca
                                    on cp.ID_CONTRACT = rca.ID_CONTRACT
                                   and cp.ID_PRODUCT = rca.ID_PRODUCT
                    where isnull(rca.OPERATING_MODE,14) in (14,15)
                      and isnull(cp.StatusCard,'') in ('CHST0','CHST5')
                      """.format(PS_id=PS_id, RBS_id=RBS_id,
                                 status_id=status_id, contract_id=contract_id))
    account = cur.fetchall()
    conn.close()
    return account

def create_account(contract_id):
    accounts = get_accounts(contract_id)
    account = []
    xml = ''
    for acc in accounts:
        account.append(dict(card_number=acc[0],
                        RBS=acc[1],
                        PS=acc[2],
                        card_data=acc[3].strftime("%Y-%m-%d"),
                        acc=acc[4],
                        acc_data=acc[5].strftime("%Y-%m-%d")))
        xml += '\n{0} {1} {2} {3} {4} {5}'.format(account[0].getkey(card_number),
                         account[0].getkey(RBS),
                         account[0].getkey(PS),
                         account[0].getkey(card_data),
                         account[0].getkey(acc),
                         account[0].getkey(acc_data))
    return xml

def create_xml(contract_id):
    


contract = 4

print(create_account(9))
print(create_account(6))                
exit()
print(get_login(contract))
print(' ')
print(create_person(get_client_id(contract)))
print(create_contract(contract))

