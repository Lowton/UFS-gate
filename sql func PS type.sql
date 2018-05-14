/*
 Функция для выдёргивания типа ПС
  по ID карточного продукта.
*/

CREATE FUNCTION dbo.RTS_GetPcCardType (@ID_CONTRACT INT)
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @ps_type VARCHAR(255) = NULL;

  	SELECT @ps_type = cpa.FIELD_STRING
      FROM CARD_PRODUCT_ADDFL cpa
      WHERE cpa.ID_FIELD = 5 -- доп. аттрибут тип ПС
        AND cpa.ID_OBJECT = (SELECT id_product FROM CARD_CONTRACT cc WHERE cc.ID_CONTRACT = @ID_CONTRACT)

      RETURN @ps_type
  END

  
GO