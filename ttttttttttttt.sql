SELECT *
  FROM RB_CONTRACT rc, RB_MODEL_ADDFL_ARRAY rm, card_contract cc
  JOIN RB_PRODUCT rp ON cc.ID_PRODUCT = rp.ID_PRODUCT_EXT
  where convert(int,rm.field_string) = rp.ID_PRODUCT
    AND rc.ID_CLIENT = cc.ID_CLIENT_OWNER


  select * from od_accounts0 where ID_ACCOUNT = 35381
SELECT * FROM card_contract WHERE ID_CLIENT_OWNER = 7245

select FIELD from CARD_CONTRACT_ADDFL_STRING
  where ID_FIELD = (select ID_FIELD from CARD_CONTRACT_ADDFL_DIC where NAME_FIELD = 'Статус карты')
    AND ID_OBJECT = 2942 /* ID договора карты */

SELECT * FROM RB_CONTRACT rc