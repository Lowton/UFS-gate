select cage_region 'Регион'
      ,cage_client 'Клиент'
      ,ps_case 'Система'
      ,case_transact 'Операция'
      ,currency 'Валюта транзакции'
      ,currency2 'Валюта ПЦ'
	  ,currency3 'Банка'
      ,money2_summ 'Сумма из ПЦ'
	  ,money3_summ 'Сумма банка'
      ,money_summ 'Сумма транзакции'
from result_ru
order by cage_region,cage_client