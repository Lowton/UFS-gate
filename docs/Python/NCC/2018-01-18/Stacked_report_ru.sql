select cage_region 'Регион'
      ,cage_client 'Клиент'
      ,ps_case 'Система'
      ,case_transact 'Операция'
      ,currency 'Валюта транзакции'
      ,currency2 'Валюта ПЦ'
      ,sum(money2_summ) 'Сумма из ПЦ'
	  ,currency3 'Валюта'
	  ,sum(money3_summ) 'Сумма из ПЦ'
from result
group by cage_region, cage_client, ps_case,case_transact,currency,currency2
order by cage_region,cage_client