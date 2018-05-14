CREATE FUNCTION dbo.RTS_RB_CLIENT_ATTRIB
  ( @FIELD VARCHAR(42),
    @OBJECT_ID INT
  )
  RETURNS VARCHAR(255)
  AS
  BEGIN
    DECLARE
      @VALUE VARCHAR(255) = NULL;

  	SELECT @field_id = cad.ID_FIELD,
           @field_type = cad.TYPE_FIELD
    FROM CLIENTS_ADDFL_DIC cad
    WHERE cad.NAME_FIELD LIKE @FIELD
    
    
    
    SELECT @VALUE = cas.FIELD
      FROM CLIENTS_ADDFL_STRING cas
      WHERE cas.ID_FIELD = @field_id                            
        AND cas.ID_OBJECT = @OBJECT_ID

      RETURN @VALUE
  END

  
GO