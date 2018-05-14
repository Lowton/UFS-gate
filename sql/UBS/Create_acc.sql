exec sp_executesql N'insert into RB_CONTRACT_ACC (ID_CONTRACT, COD_BUSINESS, NUM_CONTRACT, ACC_CONTRACT, ID_PRODUCT, NUMBRANCH, ID_CURRENCY, OPERATING_MODE, NAME_CONTRACT, BALANCE_ACC, BALANCE_CONTR, ADD_INFO) values (@ID_CONTRACT, @COD_BUSINESS, @NUM_CONTRACT, @ACC_CONTRACT, @ID_PRODUCT, @NUMBRANCH, @ID_CURRENCY, @OPERATING_MODE, @NAME_CONTRACT, @BALANCE_ACC, @BALANCE_CONTR, @ADD_INFO)',N'@ID_CONTRACT int,@COD_BUSINESS varchar(4),@NUM_CONTRACT varchar(5),@ACC_CONTRACT varchar(20),@ID_PRODUCT int,@NUMBRANCH smallint,@ID_CURRENCY smallint,@OPERATING_MODE int,@NAME_CONTRACT varchar(13),@BALANCE_ACC decimal(6,4),@BALANCE_CONTR int,@ADD_INFO varchar(959)',@ID_CONTRACT=2,@COD_BUSINESS='FDEP',@NUM_CONTRACT='00001',@ACC_CONTRACT='42307810500001000001',@ID_PRODUCT=2,@NUMBRANCH=1,@ID_CURRENCY=810,@OPERATING_MODE=14,@NAME_CONTRACT='Универсальный',@BALANCE_ACC=10.0000,@BALANCE_CONTR=0,@ADD_INFO='<?xml version="1.0" encoding="windows-1251" ?>
<u:UBS_TRANSFER xmlns:u="http://www.unisab.ru/ubs/system/base">
<u:P n="UbsParam" r="16">
<u:I4 n="Идентификатор" v="3"/>
<u:DT n="Дата окончания договора" v="2023-02-15T00:00:00.000"/>
<u:S n="Количество оставшихся пролонгаций" v="Не ограничено"/>
<u:S n="Код валюты счета" v="RUR"/>
<u:S n="Логотип" v=""/>
<u:S n="Код валюты ЦБ" v="810"/>
<u:DT n="Дата открытия" v="2018-02-15T00:00:00.000"/>
<u:I4 n="Идентификатор родительского договора" v="0"/>
<u:S n="Процентная ставка" v="0.10%"/>
<u:N n="Минимальная сумма довложения" v="-1"/>
<u:DT n="Дата окончания маратория" v="2023-02-15T00:00:00.000"/>
<u:DT n="Окончание" v="2023-02-15T00:00:00.000"/>
<u:S n="Количество пролонгаций" v="Не ограничено"/>
<u:S n="БИК банка счета" v="043678783"/>
<u:DT n="Дата открытия счета" v="2018-02-15T00:00:00.000"/>
<u:N n="Остаток в рублевом эквиваленте" v="10.0000000000000"/>
</u:P>
</u:UBS_TRANSFER>'