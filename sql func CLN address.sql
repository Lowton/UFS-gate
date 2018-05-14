/*
 Функция для формирования адресса в виде «ул. Ууууууу дд-ккк»
  по ID клиента.
*/

CREATE FUNCTION dbo.RTS_GetClnAddress (@ID_CLIENT INT)
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @address VARCHAR(255) = NULL;

    SELECT @address = cca.TYPE_STREET + '. ' + cca.NAME_STREET + ' ' + cca.NUM_BUILDING + '-' + cca.NUM_FLAT
      FROM COM_CLIENTS_ADDRESS cca
      WHERE cca.ID_CLIENT = @ID_CLIENT

      RETURN @address
  END

  
GO