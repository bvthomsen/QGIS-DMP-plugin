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
