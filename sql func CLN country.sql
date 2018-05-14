/*
 Функция для для выдёргивания страны (гражданства)
  по ID клиента.
*/

CREATE FUNCTION dbo.RTS_GetClnCountry (@ID_CLIENT INT)
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @country VARCHAR(255) = NULL;

    SELECT @country = ccas.FIELD
      FROM CLIENTS_ADDFL_STRING cas
      WHERE cas.ID_FIELD = 179 -- Это поле для определения страны
        AND cas.ID_OBJECT = @ID_CLIENT

      RETURN @country
  END

GO



