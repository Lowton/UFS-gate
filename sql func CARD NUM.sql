/*
 Функция для выдёргивания номера счёта ПЦ
  по ID договора счёта.
*/

CREATE FUNCTION dbo.RTS_GetPcCardAcc (@ID_CONTRACT INT)
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @cardaccount VARCHAR(255) = NULL;

  	SELECT @cardaccount = ccas.FIELD
      FROM CARD_CONTRACT_ADDFL_STRING ccas
      WHERE ccas.ID_FIELD = 48 -- доп. аттрибут номера телефона
        AND ccas.ID_OBJECT = @ID_CONTRACT

      RETURN @cardaccount
  END

  
GO