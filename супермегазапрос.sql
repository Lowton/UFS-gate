DECLARE @contract INT = 9

SELECT cp.num_card, cp.RBSNumber, cp.PS, cp.CARD_EXPIRE_DATE, cp.acc_main, cp.DATE_OPEN
  from (
                 select 
                   cc.ID_ACCOUNT_MAIN, rc.ID_CONTRACT,rp.ID_PRODUCT, cc.NUM_CARD,
                   (SELECT ccas.FIELD FROM CARD_CONTRACT_ADDFL_STRING ccas
                    WHERE ccas.ID_FIELD = (SELECT ccad.ID_FIELD FROM CARD_CONTRACT_ADDFL_DIC ccad
                                           WHERE ccad.NAME_FIELD = 'RBSNumber')
                      AND ccas.ID_OBJECT = cc.ID_CONTRACT) RBSNumber,
                   cc.CARD_EXPIRE_DATE,
                   (SELECT cpa.FIELD_STRING FROM CARD_PRODUCT_ADDFL cpa 
                    WHERE cpa.ID_FIELD = (SELECT cpad.ID_FIELD FROM CARD_PRODUCT_ADDFL_DIC cpad
                                          WHERE cpad.NAME_FIELD = 'Код платежной системы')
                      AND cpa.ID_OBJECT = rp.ID_PRODUCT_EXT) PS,
                   (select oa0.straccount from od_accounts0 oa0
                    where ID_ACCOUNT = cc.ID_ACCOUNT_MAIN) acc_main,
                   cc.DATE_OPEN,
                   (select FIELD from CARD_CONTRACT_ADDFL_STRING
                    where ID_FIELD = (select ID_FIELD from CARD_CONTRACT_ADDFL_DIC
                                      where NAME_FIELD = 'Статус карты')
                      and ID_OBJECT = cc.ID_CONTRACT) StatusCard
                 from
                   RB_CONTRACT rc, card_contract cc, RB_MODEL_ADDFL_ARRAY rm, RB_PRODUCT rp
                 where 
                   rc.ID_CONTRACT = @contract
                   and rc.ID_CLIENT = cc.ID_CLIENT_OWNER
                   and cc.DATE_CLOSE = '2222-01-01' -- значит, что карта не закрыта
                   and rm.ID_OBJECT = 3 -- 3 — тип договора (Договор ДБО)
                   and rm.ID_FIELD =  7 -- (SELECT rmad.ID_FIELD FROM RB_MODEL_ADDFL_DIC rmad WHERE rmad.NAME_FIELD = 'Банковские продукты')
                   and convert(int,rm.field_string) = rp.ID_PRODUCT
                   and cc.ID_PRODUCT = rp.ID_PRODUCT_EXT
                 ) cp left join RB_CONTRACT_ACC rca on cp.ID_CONTRACT = rca.ID_CONTRACT and cp.ID_PRODUCT = rca.ID_PRODUCT
                    where 
                      isnull(rca.OPERATING_MODE,14) in (14,15) -- не отключены в таблице договора ДБО клиента
                      and isnull(cp.StatusCard,'') in ('CHST0','CHST5')
                      AND LEFT(cp.NUM_CARD,6) + '******' + RIGHT(cp.NUM_CARD,4) = rca.NUM_CONTRACT
