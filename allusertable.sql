CREATE TABLE #DBO_data (id_contract INT,
  id_client INT,
  login VARCHAR(50),
  last_name VARCHAR(70),
  first_name VARCHAR(65),
  middle_name VARCHAR(25),
  inn VARCHAR(20),
  date_birth DATETIME,
  document VARCHAR(24),
  series_doc VARCHAR(20),
  reg_num VARCHAR(20),
  reg_date DATETIME,
  reg_organ VARCHAR(255),
  post_index VARCHAR(6),
  city VARCHAR(40),
  address VARCHAR(134),
  phone VARCHAR(255),
  mail VARCHAR(255),
  num_contract VARCHAR(50),
  date_begin_contract DATETIME,
  id_account_main INT,
  id_product INT,
  num_card VARCHAR(16),
  RBSnumber VARCHAR(255),
  card_expire_date DATETIME,
  ps VARCHAR(255),
  acc_main VARCHAR(25),
  acc_open_date DATETIME)

INSERT INTO #DBO_data (id_contract INT,
  id_client INT,
  login VARCHAR(50),
  last_name VARCHAR(70),
  first_name VARCHAR(65),
  middle_name VARCHAR(25),
  inn VARCHAR(20),
  date_birth DATETIME,
  document VARCHAR(24),
  series_doc VARCHAR(20),
  reg_num VARCHAR(20),
  reg_date DATETIME,
  reg_organ VARCHAR(255),
  post_index VARCHAR(6),
  city VARCHAR(40),
  address VARCHAR(134),
  phone VARCHAR(255),
  mail VARCHAR(255),
  num_contract VARCHAR(50),
  date_begin_contract DATETIME,
  id_account_main INT,
  id_product INT,
  num_card VARCHAR(16),
  RBSnumber VARCHAR(255),
  card_expire_date DATETIME,
  ps VARCHAR(255),
  acc_main VARCHAR(25),
  acc_open_date DATETIME)

(select rc.id_contract
      ,rc.id_client
      ,(SELECT ra.login FROM RB_ABONENT ra
        WHERE ra.ID_ABONENT = (SELECT rca.ID_ABONENT
                               FROM RB_CONTRACT_ABONENT rca
                               WHERE rca.ID_CONTRACT = rc.id_contract)) login
      ,c.LAST_NAME, c.FIRST_NAME, c.MIDDLE_NAME, c.INN, c.DATE_BIRTH
      ,c.DOCUMENT
      ,c.SERIES_DOC
      ,c.REG_NUM
      ,c.REG_DATE
      ,c.REG_ORGAN
      ,cca.POST_INDEX
      ,cca.NAME_CITY
      ,(cca.TYPE_STREET + '. ' + cca.NAME_STREET + ' ' + cca.NUM_BUILDING + IF (cca.NUM_FLAT) '-' + cca.NUM_FLAT;) Address
      ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                          WHERE rcas.ID_OBJECT = rc.id_contract
                            AND rcas.ID_FIELD = (select id_field FROM RB_CONTRACT_ADDFL_DIC
                                                 where name_field = 'Мобильный для ДБО')) 'SMS-phone'
      ,(SELECT field FROM RB_CONTRACT_ADDFL_STRING rcas
                          WHERE rcas.ID_OBJECT = rc.id_contract
                            AND rcas.ID_FIELD = (select id_field FROM RB_CONTRACT_ADDFL_DIC
                                                 where name_field = 'EMail клиента')) 'E-mail'
      ,rc.NUM_CONTRACT
      ,rc.DATE_BEGIN
      ,cc.ID_ACCOUNT_MAIN
      ,rp.ID_PRODUCT
      ,cc.NUM_CARD
      ,(SELECT ccas.FIELD FROM CARD_CONTRACT_ADDFL_STRING ccas
        WHERE ccas.ID_FIELD = (SELECT ccad.ID_FIELD FROM CARD_CONTRACT_ADDFL_DIC ccad
                               WHERE ccad.NAME_FIELD = 'RBSNumber')
          AND ccas.ID_OBJECT = cc.ID_CONTRACT) RBSNumber
      ,cc.CARD_EXPIRE_DATE
      ,(SELECT cpa.FIELD_STRING FROM CARD_PRODUCT_ADDFL cpa 
        WHERE cpa.ID_FIELD = (SELECT cpad.ID_FIELD FROM CARD_PRODUCT_ADDFL_DIC cpad
                              WHERE cpad.NAME_FIELD = 'Код платежной системы')
          AND cpa.ID_OBJECT = rp.ID_PRODUCT_EXT) PS
      ,(select oa0.straccount from od_accounts0 oa0
        where ID_ACCOUNT = cc.ID_ACCOUNT_MAIN) acc_main
      ,cc.DATE_OPEN

from rb_contract rc
LEFT JOIN CLIENTS c ON c.ID_CLIENT = rc.ID_CLIENT
LEFT JOIN COM_CLIENTS_ADDRESS cca ON c.ID_CLIENT = cca.ID_CLIENT
LEFT JOIN CARD_CONTRACT cc ON rc.ID_CLIENT = cc.ID_CLIENT_OWNER AND cc.DATE_CLOSE = '2222-01-01'
LEFT JOIN RB_PRODUCT rp ON rp.ID_PRODUCT_EXT = cc.ID_PRODUCT
LEFT join RB_CONTRACT_ACC rca on rc.ID_CONTRACT = rca.ID_CONTRACT and rp.ID_PRODUCT = rca.ID_PRODUCT and rca.NUM_CONTRACT = (LEFT(cc.NUM_CARD,6) + '******' + RIGHT(cc.NUM_CARD,4))
LEFT JOIN RB_MODEL_ADDFL_ARRAY rmaa ON convert(int,rmaa.field_string) = rp.ID_PRODUCT

where isnull(rca.OPERATING_MODE,14) in (14,15) -- не отключены в таблице договора ДБО клиента
  and isnull((select FIELD from CARD_CONTRACT_ADDFL_STRING
              where ID_FIELD = (select ID_FIELD from CARD_CONTRACT_ADDFL_DIC
                                 where NAME_FIELD = 'Статус карты')
                and ID_OBJECT = cc.ID_CONTRACT),'') in ('CHST0','CHST5')
  AND rmaa.ID_FIELD = 7
  AND rmaa.ID_OBJECT = 3
  AND cca.TYPE_ADDRESS = 103)