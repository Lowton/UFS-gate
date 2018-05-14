from pyodbc import connect
from config import ubs_connect, sourceFile, outputFile
from datetime import datetime
from log import log
import xml_source

class faktura_xml_reqest:
    u'Класс определяющий все данные для создания xml-запроса в Фактуру'

    def __init__(self, id_contarct):
        self.id_contract = id_contarct
        self.id_client = self.get_client_id()
        self.login = self.get_login()
        self.pasport_data = get_pasport()
        self.pasport_type = self.pasport_data.getkey(pasport)
        self.pasport_serial = self.pasport_data.getkey(serial)
        self.pasport_number = self.pasport_data.getkey(number)
        self.pasport_date = self.pasport_data.getkey(date)
        self.pasport_dept = self.pasport_data.getkey(dept)
        self.address_data = self.get_address()
        self.address_country = self.address_data.getkey(country)
        self.address_index = self.address_data.getkey(index)
        self.address_city = self.address_data.getkey(city)
        self.address_street = self.address_data.getkey(street)
        self.address_mail = self.address_data.getkey(mail)
        self.address_phone = self.address_data.getkey(phone)
        self.person_data = self.get_person()
        self.person_first_name = self.person_data(first_name)
        self.person_middle_name = self.person_data(middle_name)
        self.person_last_name = self.person_data(last_name)
        self.person_inn = self.person_data(inn)
        self.person_birthday = self.person_data(birthday)
        self.contract_data = get_contract()
        self.contract_number = self.contract_data.getkey(num)
        self.contract_date = self.contract_data.getkey(open_date)
        self.contract_phone = self.contract_data.getkey(phone)
        self.account_data = self.get_accounts()

    def get_client_id(self):
        conn = connect(ubs_connect)
        cur = conn.cursor()
        cur.execute("""select id_client
                       from rb_contract
                       where id_contract = {}
                       """.format(self.id_contract))
        client_id = cur.fetchone()[0]
        conn.close()
        return client_id

    def get_id(self, table, value):
        request_id = """(select id_field from {table}
                       where name_field = '{value}')
                       """.format(table=table, value=value)
        return request_id

    def get_login():
        conn = connect(ubs_connect)
        cur = conn.cursor()
        cur.execute("""SELECT ra.login FROM RB_ABONENT ra
                       WHERE ra.ID_ABONENT = (
                             SELECT rca.ID_ABONENT
                             FROM RB_CONTRACT_ABONENT rca
                             WHERE rca.ID_CONTRACT = {})
                    """.format(self.id_contract))
        login = cur.fetchone()[0]
        conn.close()
        return login

    def get_pasport():
        conn = connect(ubs_connect)
        cur = conn.cursor()
        cur.execute("""select document,reg_num,series_doc,
                              reg_date,reg_organ
                       from clients
                       where id_client = {}""".format(self.id_client))
        pasport = cur.fetchone()
        conn.close()
        
        pasport_data = dict(document = 'Паспорт' if \
                            pasport[0] == 'Паспорт гражданина РФ' else Null,
                            serial = pasport[2]
                            number = pasport[1]
                            date = pasport[3].strftime("%Y-%m-%d")
                            dept = pasport[4])
        return pasport_data

    def get_address():
        country_id = self.get_id('CLIENTS_ADDFL_DIC','Гражданство (подданство)')
        phone_id = self.get_id('RB_CONTRACT_ADDFL_DIC','Мобильный для ДБО')
        email_id = self.get_id('RB_CONTRACT_ADDFL_DIC','EMail клиента')

        conn = connect(ubs_connect)
        cur = conn.cursor()
        req = """select (select cas.FIELD FROM CLIENTS_ADDFL_STRING cas 
                         WHERE cas.ID_FIELD = {country_id}
                         AND cas.ID_OBJECT = {client_id})
                        ,cca.post_index, cca.name_city
                        ,(cca.TYPE_STREET + '. ' + cca.NAME_STREET + ' '
                           + cca.NUM_BUILDING + '-' + cca.NUM_FLAT)
                        ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                          WHERE  rcas.ID_OBJECT = (SELECT rc.ID_CONTRACT
                                                   FROM RB_CONTRACT rc
                                                   WHERE rc.ID_CLIENT = {client_id})
                          AND rcas.ID_FIELD = {phone_id})
                        ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                          WHERE  rcas.ID_OBJECT = (SELECT rc.ID_CONTRACT
                                                   FROM RB_CONTRACT rc
                                                   WHERE rc.ID_CLIENT = {client_id})
                          AND rcas.ID_FIELD = {email_id})
                  from COM_CLIENTS_ADDRESS cca
                  where id_client = {client_id}""".format(country_id=country_id,
                                                          client_id=self.id_client,
                                                          phone_id=phone_id,
                                                          email_id=email_id)
        cur.execute(req)
        address = cur.fetchone()
        conn.close()
        
        address_data = dict(country=address[0],index=address[1],
                       city = address[2],street = address[3]
                       mail = address[5] if address[5] else '',
                       phone = address[4] if address[4] else '')
        return address_data

    def get_person():
        conn = connect(ubs_connect)
        cur = conn.cursor()
        cur.execute("""SELECT c.FIRST_NAME, c.MIDDLE_NAME,
                              c.LAST_NAME, c.INN, c.DATE_BIRTH
                       FROM CLIENTS c
                       WHERE c.ID_CLIENT = {}""".format(self.id_client))
        person = cur.fetchone()
        conn.close()
        
        person_data = dict(first_name = person[0], middle_name = person[1],
                           last_name = person[2], inn = person[3],
                           birthday = person[4].strftime("%Y-%m-%d"))        
        return person_data

    def get_contract():
        phone_id = get_id('RB_CONTRACT_ADDFL_DIC','Мобильный для ДБО')

        conn = connect(ubs_connect)
        cur = conn.cursor()
        cur.execute("""SELECT rc.NUM_CONTRACT, rc.DATE_BEGIN
                            ,(SELECT rcas.FIELD
                              FROM RB_CONTRACT_ADDFL_STRING rcas
                              WHERE rcas.ID_OBJECT = {0}
                              AND rcas.ID_FIELD = {1})
                       FROM RB_CONTRACT rc
                       WHERE ID_CONTRACT = {0}
                    """.format(self.id_contract, phone_id))
        contract = cur.fetchone()
        conn.close()
        
        contract_data = dict(contract = get_contract(contract_id),
                             num = contract[0],
                             open_date = contract[1].strftime("%Y-%m-%d"),
                             phone = contract[2] if contract[2] else '')
        return contract_data

    def get_accounts():
        PS_id = get_id('CARD_PRODUCT_ADDFL_DIC','Код платежной системы')
        RBS_id = get_id('CARD_CONTRACT_ADDFL_DIC','RBSNumber')
        status_id = get_id('CARD_CONTRACT_ADDFL_DIC','Статус карты')

        conn = connect(ubs_connect)
        cur = conn.cursor()
        req = """SELECT DISTINCT cp.num_card, cp.RBSNumber,
                                 cp.PS, cp.CARD_EXPIRE_DATE,
                                 cp.acc_main, cp.DATE_OPEN
                 from (select cc.ID_ACCOUNT_MAIN, rc.ID_CONTRACT,
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
                        status_id=status_id, contract_id=contract_id)
        cur.execute(req)
        accounts = cur.fetchall()
        conn.close()

        account_data = []
        for acc in accounts:
            account_data.append(dict(card_number=acc[0],
                                     RBS=acc[1],
                                     PS=acc[2],
                                     card_data=acc[3].strftime("%Y-%m-%d"),
                                     acc=acc[4],
                                     acc_data=acc[5].strftime("%Y-%m-%d")))
        account_data = dict()
        return account_data

    def create_contract_xml():
        pass
        
                
                                


fxr = faktura_xml_reqest(5)
print(fxr.id_contract, fxr.id_client)
