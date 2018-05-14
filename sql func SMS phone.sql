/*
 Функция для выдёргивания номера телефона для
  SMS-оповещений по ID договора счёта.
*/

CREATE FUNCTION dbo.RTS_GetSMSphone (@ID_CONTRACT INT)
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @phone VARCHAR(255) = NULL;

  	SELECT @phone = ccas.FIELD
      FROM CARD_CONTRACT_ADDFL_STRING ccas
      WHERE ccas.ID_FIELD = 51 -- доп. аттрибут номера телефона
        AND ccas.ID_OBJECT = @ID_CONTRACT

      RETURN @phone
  END

  
GO