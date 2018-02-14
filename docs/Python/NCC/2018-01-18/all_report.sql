select cage_region 'Регион'
      ,cage_client 'Клиент'
      ,ps_case 'Система'
      ,case_transact 'Операция'
      ,currency 'Валюта транзакции'
      ,currency2 'Валюта ПЦ'
      ,money2_summ 'Сумма из ПЦ'
      ,money_summ 'Сумма транзакции'
from result
order by cage_region,cage_client