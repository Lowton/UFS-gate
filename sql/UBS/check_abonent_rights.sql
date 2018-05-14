exec sp_executesql N'select K.ID_KIND_DOC
                        ,K.SID_KIND_DOC
                        ,K.NAME_KIND_DOC
                        ,case when ABN.TYPE_ABONENT = 0 
                                then  31 
                                else 3
                         end
                        ,isnull(tblSetup.ID_KIND_DOC, 0)
                        ,ABN.TYPE_ABONENT
                  from RB_KIND_DOCUMENT K
                       ,( select ID_KIND_DOC
                          from RB_KIND_DOCUMENT
                          where ID_KIND_DOC in (@ID_KIND_DOC1)
                        ) tblAcess
                        
                        full join ( select K.ID_KIND_DOC, 31 ACCESS_MASK
                                    from fn_OGO_READ_SETTING_TABLE(''Дистанционное банковское обслуживание'', ''Доступный функционал'') fn1 
                                        ,fn_OGO_READ_SETTING_TABLE(''Дистанционное банковское обслуживание'', ''Доступный функционал'') fn2
                                        , RB_KIND_DOCUMENT K
                                    where fn1.INDEX_ROW = fn2.INDEX_ROW
                                      and fn1.INDEX_COLUMN = 1
                                      and fn2.INDEX_COLUMN = 2 and fn1.VALUE = K.SID_KIND_DOC
                                      and fn2.VALUE = 1
                                  ) tblSetup
                        on tblSetup.ID_KIND_DOC = tblAcess.ID_KIND_DOC
                       ,RB_ABONENT ABN
                  where ABN.ID_ABONENT = @ID_ABONENT
                    and ISNULL(tblAcess.ID_KIND_DOC, tblSetup.ID_KIND_DOC) = K.ID_KIND_DOC
                  order by K.NAME_KIND_DOC',N'@ID_CONTRACT int,@ID_ABONENT int,@ID_KIND_DOC1 int',@ID_CONTRACT=0,@ID_ABONENT=4,@ID_KIND_DOC1=0