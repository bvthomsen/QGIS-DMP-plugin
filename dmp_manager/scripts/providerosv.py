#                                    setting = sd.cbDatabase.itemData(sd.cbDatabase.currentIndex())
#                                    metadata = QgsProviderRegistry.instance().providerMetadata(setting[0])
#                                    conn = metadata.findConnection(setting[1])
#                                    if sd.cbSchema.currentIndex() >=0:
#                                        spart = '"{}".'.format(sd.cbSchema.currentText())
#                                    else:
#                                        spart = ''                                
providerType = 'spatialite'
connectionId = 'skadesmodel.sqlite'

tblCurrent = 'raastofomr'
tblReference = '__reference__raastofomr'
fldPK = 'objekt-id'
fldGeom= 'geom'

c = QgsProviderRegistry.instance().providerMetadata(providerType).connections()[connectionId]
o = QgsAbstractDatabaseProviderConnection.SqlVectorLayerOptions()
o.primaryKeyColumns = [fldPK]
o.geometryColumn = fldGeom

o.sql = 'SELECT ref.* FROM {ref} ref LEFT JOIN {cur} cur on ref."{pk}" = cur."{pk}" WHERE cur."{pk}" IS NULL'.format(ref=tblReference, cur=tblCurrent, pk=fldPK)
o.layerName='Deleted'
vl = c.createSqlVectorLayer(o)
if vl.isValid():QgsProject.instance().addMapLayer(vl)

o.sql = 'SELECT cur.* FROM {cur} cur LEFT JOIN {ref} ref on cur."{pk}" = ref."{pk}" WHERE ref."{pk}" IS NULL'.format(ref=tblReference, cur=tblCurrent, pk=fldPK)
o.layerName='Inserted'
vl = c.createSqlVectorLayer(o)
if vl.isValid():QgsProject.instance().addMapLayer(vl)

o.sql = 'SELECT cur.* FROM {cur} cur LEFT JOIN {ref} ref on cur."{pk}" = ref."{pk}" WHERE ref."{pk}" IS NOT NULL EXCEPT SELECT ref.* FROM {ref} ref LEFT JOIN {cur} cur on cur."{pk}" = ref."{pk}" WHERE cur."{pk}" IS NOT NULL'.format(ref=tblReference, cur=tblCurrent, pk=fldPK)
o.layerName='Modified_current'
vl = c.createSqlVectorLayer(o)
if vl.isValid():QgsProject.instance().addMapLayer(vl)

o.sql = 'SELECT ref.* FROM {ref} ref LEFT JOIN {cur} cur on cur."{pk}" = ref."{pk}" WHERE cur."{pk}" IS NOT NULL EXCEPT SELECT cur.* FROM {cur} cur LEFT JOIN {ref} ref on cur."{pk}" = ref."{pk}" WHERE ref."{pk}" IS NOT NULL'.format(ref=tblReference, cur=tblCurrent, pk=fldPK)
o.layerName='Modified_reference'
vl = c.createSqlVectorLayer(o)
if vl.isValid():QgsProject.instance().addMapLayer(vl)



                                if sd.cbDatabase.currentIndex() >=0:

                                    setting = sd.cbDatabase.itemData(sd.cbDatabase.currentIndex())
                                    metadata = QgsProviderRegistry.instance().providerMetadata(setting[0])
                                    conn = metadata.findConnection(setting[1])

                                    if sd.cbSchema.currentIndex() >=0:
                                        spart = '"{}".'.format(sd.cbSchema.currentText())
                                    else:
                                        spart = ''                                

                                    wpart = self.genDictWhere(ml.name(), r'cur."{0}" {1} ref."{0}"', r'=', 'and', 'geom', 'not (', ')')


                                    try:                                    
                                        conn.execSql ('DROP VIEW {0}{1}{2}'.format(spart,'__inserted__',ml.name()));
                                    except:
                                        pass
                                    try:                                    
                                        conn.execSql ('DROP VIEW {0}{1}{2}'.format(spart,'__deleted__',ml.name()));
                                    except:
                                        pass
                                    try:                                    
                                        conn.execSql ('DROP VIEW {0}{1}{2}'.format(spart,'__modified_ref__',ml.name()));
                                    except:
                                        pass
                                    try:                                    
                                        conn.execSql ('DROP VIEW {0}{1}{2}'.format(spart,'__modified_cur__',ml.name()));
                                    except:
                                        pass
                                         
                                    txt = 'CREATE VIEW {0}{1}{2} AS select cur.* from {0}{2} cur left join {0}{3}{2} ref on cur."{4}" = ref."{4}" where ref."{4}" is NULL'.format(spart,'__inserted__',ml.name(),'__reference__',spd["PKName"])
                                    logI(txt)
                                    conn.execSql (txt);

                                    txt = 'CREATE VIEW {0}{1}{2} AS select ref.* from {0}{3}{2} ref left join {0}{2} cur on cur."{4}" = ref."{4}" where cur."{4}" is NULL'.format(spart,'__deleted__',ml.name(),'__reference__',spd["PKName"])
                                    logI(txt)
                                    conn.execSql (txt);

                                    txt = 'CREATE VIEW {0}{1}{2} AS select ref.* from {0}{3}{2} ref left join {0}{2} cur on cur."{4}" = ref."{4}" where {5}'.format(spart,'__modified_ref__',ml.name(),'__reference__',spd["PKName"],wpart)
                                    logI(txt)
                                    conn.execSql (txt);

                                    txt = 'CREATE VIEW {0}{1}{2} AS select cur.* from {0}{2} cur left join {0}{3}{2} ref on cur."{4}" = ref."{4}" where {5}'.format(spart,'__modified_cur__',ml.name(),'__reference__',spd["PKName"],wpart)
                                    logI(txt)
                                    conn.execSql (txt);
