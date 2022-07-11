# -*- coding: utf-8 -*-
from json import load, dump, dumps, loads
import requests, string, os.path, random

from PyQt5.QtCore import (QCoreApplication,
                          Qt,
                          QDateTime,
                          QPointF,
                          QVariant,
                          QUrl)
                          
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPolygonF
from PyQt5.QtNetwork import QNetworkRequest 

from qgis.utils import iface
from qgis.core import (QgsMessageLog,
                       Qgis,
                       QgsVectorLayer,
                       QgsProject,
                       QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform,QgsGeometry,
                       QgsField, 
                       QgsExpressionContextUtils,
                       QgsFeature,
                       QgsPointXY,
                       QgsVectorLayerExporter,
                       QgsNetworkAccessManager,
                       QgsFeatureRequest,
                       QgsLayerTreeGroup,
                       QgsAbstractDatabaseProviderConnection,
                       QgsProviderRegistry,
                       QgsDataSourceUri)

trClassName = ''

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def zoomToFeature (lid, fid):
    """Replace with explanation"""

    layer = QgsProject.instance().mapLayer(lid)
    feat = layer.getFeature(fid)
    geom = feat.geometry()
    
    sourceCrs = layer.crs().authid()
    destCrs = iface.mapCanvas().mapSettings().destinationCrs().authid()
    if sourceCrs != destCrs:
        x = QgsCoordinateTransform(QgsCoordinateReferenceSystem(sourceCrs), QgsCoordinateReferenceSystem(destCrs), QgsProject.instance())
        geom.transform(x)

    box = geom.boundingBox()
    box.scale(1.2)
    iface.mapCanvas().setExtent(box)
    iface.mapCanvas().refresh()

def trInit(className):
    """Replace with explanation"""
    global trClassName
    trClassName = className


# noinspection PyMethodMayBeStatic
def tr(message):
    """Helper to translate strings"""

    global trClassName
    return QCoreApplication.translate(trClassName, message)


def findLayerVariableValue(ename, evalue):
    """Find layer containing specific environment variable value"""

    if ename and evalue:
        for ltLayer in QgsProject.instance().layerTreeRoot().findLayers():
            if evalue == QgsExpressionContextUtils.layerScope(ltLayer.layer()).variable(ename):
                return ltLayer, ltLayer.layer()

    return None, None


def assignLayerVariable(layer, ename, evalue):
    """Assign name/value pair to specific layer"""

    if layer and ename and evalue:
        QgsExpressionContextUtils.setLayerVariable(layer, ename, evalue)

def evalLayerVariable(layer, ename):
    """Evaluate variable by name for specific layer"""

    if layer and ename:
        if QgsExpressionContextUtils.layerScope(layer).hasVariable(ename):
            return QgsExpressionContextUtils.layerScope(layer).variable(ename)
    return None

def logI(mess, tab=None):
    """Replace with explanation"""

    global trClassName
    tab = tab or trClassName
    QgsMessageLog.logMessage(mess, tab, Qgis.Info, False)


def logW(mess, tab=None):
    """Replace with explanation"""

    global trClassName
    tab = tab or trClassName
    QgsMessageLog.logMessage(mess, tab, Qgis.Warning, True)


def logC(mess, tab=None):
    """Replace with explanation"""

    global trClassName
    tab = tab or trClassName
    QgsMessageLog.logMessage(mess, tab, Qgis.Critical, True)


def messI(message, prefix=None, duration=5):
    """Replace with explanation"""

    global trClassName
    prefix = prefix or trClassName
    iface.messageBar().pushMessage(prefix, message, Qgis.Info, duration)
    iface.mainWindow().repaint()


def messW(message, prefix=None, duration=20):
    """Replace with explanation"""

    global trClassName
    prefix = prefix or trClassName
    iface.messageBar().pushMessage(prefix, message, Qgis.Warning, duration)
    iface.mainWindow().repaint()


def messC(message, prefix=None, duration=30):
    """Replace with explanation"""

    global trClassName
    prefix = prefix or trClassName
    iface.messageBar().pushMessage(prefix, message, Qgis.Critical, duration)
    iface.mainWindow().repaint()


def xstr(s, r=''):
    """Replace with explanation"""

    return r if not s else str(s)


def createGroup(groupName, root, top=False):
    """TBD"""

    group = root.findGroup(groupName)

    if group is None:
        if top:
            group = root.insertGroup(0, groupName)            
        else:
            group = root.addGroup(groupName)
    return group


def removeGroup(groupName, root):
    """Replace with explanation"""

    group = root.findGroup(groupName)
    if group is not None:
        root.removeChildNode(group)


def removeGroupLayer(groupName, layer, root):
    """Replace with explanation"""

    group = root.findGroup(groupName)
    if group is not None:
        # Find layer if exists
        ln = group.findLayer(layer)
        if layer is not None:
            group.removeChildNode(ln)


def clearGroupLayer(groupName, layer, root):
    """Replace with explanation"""

    group = root.findGroup(groupName)
    if group is not None:
        ln = group.findLayer(layer)
        if ln is not None:
            ln.layer().dataProvider.truncate()
            return ln

    return None


def cnvobj2obj(gobj, epsg_in, epsg_out):
    """Replace with explanation"""

    if epsg_in == epsg_out:
        return gobj

    else:
        crsSrc = QgsCoordinateReferenceSystem(epsg_in)
        crsDest = QgsCoordinateReferenceSystem(epsg_out)
        xform = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())
        return gobj.transform(xform)


def cnvobj2wkt(gobj, epsg_in, epsg_out):
    """TBD"""

    return cnvobj2obj(gobj, epsg_in, epsg_out).asWkt()


def cnvwkt2obj(wkt, epsg_in, epsg_out):
    """TBD"""

    return cnvobj2obj(QgsGeometry.fromWkt(wkt), epsg_in, epsg_out)


def cnvwkt2wkt(wkt, epsg_in, epsg_out):
    """TBD"""

    return cnvobj2wkt(QgsGeometry.fromWkt(wkt), epsg_in, epsg_out)


def wkbtype2simple(wtype):
    """TBD"""

    my_WkbType = {0: 'pnt', 1: 'pnt', 2: 'lin', 3: 'pol', 4: 'pnt', 5: 'lin', 6: 'pol'}
    return my_WkbType[wtype]


def wkbtype2str(wtype):
    """TBD"""

    my_WkbType = {0: 'Unknown', 1: 'Point', 2: 'LineString', 3: 'Polygon', 4: 'MultiPoint', 5: 'MultiLineString', 6: 'MultiPolygon', 100: 'NoGeometry'}
    return my_WkbType[wtype]


def read_config(filename):
    """TBD"""

    file = open(filename)
    dictF = load(file)
    file.close()
    return dictF


def write_config(filename, config):
    """TBD"""

    file = open(filename, mode='w', encoding='utf8')
    dump(config, file, indent=4)
    file.close()


def createRequestLog(ename, evalue, lname, root=None, top=True, style=None, dbConn=None, schName=None):
    """TBD"""

    ltl, ml = findLayerVariableValue(ename, evalue)

    if ml is None:
        fields = [QgsField("operation", QVariant.String),
                  QgsField("url", QVariant.String),
                  QgsField("package", QVariant.String),
                  QgsField("status_code", QVariant.String),
                  QgsField("dict", QVariant.String),
                  QgsField("timestamp", QVariant.String),
                  QgsField("errortext", QVariant.String),
                  QgsField("module", QVariant.String)]

        if dbConn is None:
            ml = QgsVectorLayer("None", lname, "memory")
            ml.dataProvider().addAttributes(fields)
            ml.updateFields()
        else:
            if not dbConn.tableExists(schName, lname): dbConn.createVectorTable(schName, lname, fields, 100)
            options = QgsAbstractDatabaseProviderConnection.SqlVectorLayerOptions()
            options.sql = 'SELECT * from FROM "{}"."{}"'.format(schName, lname)
            options.primaryKeyColumns = []
            options.geometryColumn = ''
            ml = conn.createSqlVectorLayer(options)             
    ltl = addLayer2Tree(root, ml, top, ename, evalue, style)

    return ltl, ml


def handleRequest_new(urlstr, isPost=False, headers=None, package=None, loglayer=None, module='', authconf = ''):
    """TBD"""

    nam = QgsNetworkAccessManager()
    url = QUrl(urlstr)
    req = QNetworkRequest(url)

    if headers:
        for key, value in headers.items():
            req.setRawHeader(bytes(key, "utf-8"), bytes(value, "utf-8"))
 
    resp = nam.blockingPost(req, bytes(json.dumps(package) if package else None, "utf-8"), authconf) if isPost else nam.blockingGet(req, authconf)
    scode = resp.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    dictR = loads(str(resp.content(), "utf-8" )) if scode == 200 else None

    if loglayer:

        stime = QDateTime.currentDateTime().toString(Qt.ISODate)
        feat = QgsFeature(loglayer.fields())
        feat['operation'] = 'post' if isPost else 'get'
        feat['url'] = urlstr
        feat['package'] = dumps(package, indent=2) if package else ''
        feat['status_code'] = str(scode)
        feat['dict'] = dumps(dictR, indent=2)[:100000] if dictR else ''
        feat['timestamp'] = stime
        feat['module'] = module
        loglayer.dataProvider().addFeatures([feat])

    return scode, dictR

def handleRequest_old2(urlstr, isPost=False, headers=None, package=None, loglayer=None, module='', authconf = ''):
    """TBD"""

    nam = QgsNetworkAccessManager()
    url = QUrl(urlstr)
    req = QNetworkRequest(url)

    if headers:
        for key, value in headers.items():
            req.setRawHeader(bytes(key, "utf-8"), bytes(value, "utf-8"))
 
    resp = nam.blockingPost(req, bytes(json.dumps(package) if package else None, "utf-8"), authconf) if isPost else nam.blockingGet(req, authconf)
    scode = resp.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    dictR = loads(str(resp.content(), "utf-8" )) if scode == 200 else None

    if loglayer:

        stime = QDateTime.currentDateTime().toString(Qt.ISODate)
        feat = QgsFeature(loglayer.fields())
        feat['operation'] = 'post' if isPost else 'get'
        feat['url'] = urlstr
        feat['package'] = dumps(package, indent=2) if package else ''
        feat['status_code'] = str(scode)
        feat['dict'] = dumps(dictR, indent=2)[:100000] if dictR else ''
        feat['timestamp'] = stime
        feat['module'] = module
        loglayer.dataProvider().addFeatures([feat])

    return scode, dictR

def handleRequest    (url, method='get', headers=None, package=None, loglayer=None, module=''):
    """TBD"""
    
    method = method.lower()
    
    if method == 'post':
        r = requests.post(url, json=package, headers=headers)
 
    elif method == 'get':
        r = requests.get(url, headers=headers)

    elif method == 'patch':
        r = requests.patch(url, json=package, headers=headers)

    elif method == 'delete':
        r = requests.delete(url, headers=headers)

    scode = r.status_code
    try:
        dictR = r.json() 
    except:
        dictR = {}

    if loglayer:

        stime = QDateTime.currentDateTime().toString(Qt.ISODate)

        feat = QgsFeature(loglayer.fields())
        feat['operation'] = method
        feat['url'] = url
        feat['package'] = dumps(package, indent=2) if package else ''
        feat['status_code'] = str(scode)
        feat['dict'] = dumps(dictR, indent=2)[:100000] if dictR else ''
        feat['timestamp'] = stime
#        feat['errortext'] = r.text
        feat['module'] = module
        loglayer.dataProvider().addFeatures([feat])

    return scode, dictR

def handleRequest2    (url, method='get', headers=None, package=None, loglayer=None, module=''):
    """TBD"""
    
    method = method.lower()
    
    if method == 'post':
        if headers:
            r = requests.post(url, json=package, headers=headers)\
                if package else requests.post(url, headers=headers)
        else:
            r = requests.post(url, json=package)\
                if package else requests.post(url)

    elif method == 'get':
        r = requests.get(url, headers=headers)\
            if headers else requests.get(url)

    elif method == 'patch':
        if headers:
            r = requests.patch(url, json=package, headers=headers)\
                if package else requests.patch(url, headers=headers)
        else:
            r = requests.patch(url, json=package)\
                if package else requests.patch(url)

    elif method == 'delete':
        r = requests.delete(url, headers=headers)\
            if headers else requests.delete(url)

    scode = r.status_code
    dictR = r.json() if r.status_code == 200 else None

    if loglayer:

        stime = QDateTime.currentDateTime().toString(Qt.ISODate)

        feat = QgsFeature(loglayer.fields())
        feat['operation'] = method
        feat['url'] = url
        feat['package'] = dumps(package, indent=2) if package else ''
        feat['status_code'] = str(scode)
        feat['dict'] = dumps(dictR, indent=2)[:100000] if dictR else ''
        feat['timestamp'] = stime
        feat['module'] = module
        loglayer.dataProvider().addFeatures([feat])

    return scode, dictR


def mapperExtent(epsg):
    """ Find extend of Mapper in predefined crs"""

    extent = iface.mapCanvas().extent()

    crsSrc = iface.mapCanvas().mapSettings().destinationCrs()
    crsDest = QgsCoordinateReferenceSystem("EPSG:{}".format(epsg))

    if crsSrc != crsDest:
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        extent = xform.transform(extent)

    xmi = extent.xMinimum()
    xma = extent.xMaximum()
    ymi = extent.yMinimum()
    yma = extent.yMaximum()

    coordinates = [xmi, yma, xma, yma, xma, ymi, xmi, ymi, xmi, yma]
    point = QPointF()
    list_polygon = QPolygonF()

    for x in range(len(coordinates)):
        if x % 2 == 0:
            point.setX(coordinates[x])
            point.setY(coordinates[x + 1])
            list_polygon.append(point)

    return QgsGeometry.fromQPolygonF(list_polygon)


def createDateTimeName(name):
    """TBD"""
    return '{}_{}'.format(xstr(name), QDateTime.currentDateTime().toString('yyyy_MM_dd_hh_mm_ss_zzz'))


def createDmpLayer(uristr, contype, dicta, temanr, epsg):
    """TBD"""

    pass


def createMemLayer(dicta, temanr, epsg):
    """TBD"""

    # Find dictianary element using temanr id
    title = None
    tname = None
    gtype = None

    for d in dicta["temakoder"]:
        if d["id"] == str(temanr):
            e = d["attributes"]
            title = e["title"]
            tname = e["name"]
            gtype = e["geometry-type"]
            break

    if title:

        # Create memory layer
        vl = QgsVectorLayer('{}?crs=epsg:{}&index=yes'.format(gtype,
                            str(epsg).upper().replace('EPSG:', '')),
                            tname, 'memory')

        ll = {}
        pr = vl.dataProvider()

        fl1, ll1 = createFieldListAttributter(dicta["attributter"])
        pr.addAttributes(fl1)

        fl2, ll2 = createFieldListTemaAttributter(dicta["temaattributter"], temanr)
        pr.addAttributes(fl2)

        vl.updateFields()

        ll.update(ll1)
        ll.update(ll2)
        
        return title, vl, ll

    # Error, temakode not found
    messC('Error creating memory layer, temanr: {} not found'.format(temanr))
    return None, None, None


def createFieldListAttributter(dictaa):
    """TBD"""

    fl = []
    ll = {}

    for d in dictaa:

        if d["id"] != 'temaattributter':

            f, le, tt = createField(d["attributes"])
            fl.append(f)
            if le:
                ll[tt] = le

    return fl, ll


def createFieldListTemaAttributter(dictata, temanr):
    """TBD"""

    fl = []
    ll = {}

    for d in dictata:

        if d["relationships"]["temakode"]["data"]["id"] == str(temanr):

            f, le, tf = createField(d["attributes"])
            fl.append(f)
            if le:
                ll[tf] = le

    return fl, ll


def createField(e):
    """TBD"""

    f = QgsField()
    le = None
    tf = None

    f.setName(e["name"])
    f.setAlias(e["title"])

    if e["data-type"] == "string":
        f.setType(QVariant.String)

    elif e['data-type'] == "uuid":
        f.setType(QVariant.String)

    elif e['data-type'] == "datetime":
        f.setType(QVariant.DateTime)

    elif e['data-type'] == "number":
        f.setType(QVariant.Int)

    elif e['data-type'] == "domain":
        f.setType(QVariant.String)
        le, tf = createMemLookup(e["domain"], e["name"], e["title"])

    elif e['data-type'] == "domain-multi":
        f.setType(QVariant.String)
        le, tf = createMemLookup(e["domain"], e["name"], e["title"])

    else:
        f.setType(QVariant.String)

    if e["default"]:
        f.setDefaultValueDefinition(e["default"])

    return f, le, tf


def createMemLookup(domain, tfield, ttitle):
    """TBD"""

    vl = QgsVectorLayer('None', tfield, 'memory')

    pr = vl.dataProvider()
    pr.addAttributes([QgsField("lk_key", QVariant.String), QgsField("lk_value", QVariant.String)])
    vl.updateFields()

    fetl = []
    for k, v in domain.items():
        fet = QgsFeature(vl.fields())
        fet.setAttributes([k, v])
        fetl.append(fet)
    pr.addFeatures(fetl)

    return vl, ttitle

def updateLayer(layer, dicto, pkid = None, pkquote = None, value = None):
    """Converts an dictionary object to a layer feature and update the layer by inserting or updating"""

    j = 0
    d = dicto["data"]
    f = QgsFeature(layer.fields())
    e = d["attributes"]
    
    for k, v in e.items():
        if k == "temaattributter":
            for k2, v2 in v.items():
                logI ('TemaAttributter: ' + k2 + '~ ' + str(v2))
                f.setAttribute(k2, v2)
        elif k == "shape":
            f.setGeometry(cnvGJ2QgsGeometry(v))
        else:
            logI ('Attributter: ' + k + '~ ' + str(v))
            f.setAttribute(k, v)
    if pkid:
        pkids = layer.primaryKeyAttributes() 
        logI ('pkid = ' + str(pkid) + ', value = ' + str(value))
        layer.startEditing()
        expression = '"{0}"={2}{1}{2}'.format(pkid,value,pkquote)
        logI ('expression: '+ expression)
        for g in layer.getFeatures(QgsFeatureRequest().setFilterExpression(expression)): 
            logI ('g.id = ' + str(g.id()))
            for ff in f.fields().names(): 
                if f.fields().indexFromName(ff) not in pkids:
                    g.setAttribute(ff, f[ff])  
                    logI('......' + ff + ' :: ' + str(f[ff]) + ' :: ' + str(g[ff]))
            layer.updateFeature(g)
        layer.commitChanges()
    else:
        logI ('insert uden pkid')
        dp = layer.dataProvider()
        dp.addFeatures([f])

def updateLayers (layerc, layerr, dicto, pkid, pkquote, value):
    """Converts an dictionary object to a layer feature and update the layers by inserting or updating"""

    logI ('I updateLayers, layerc = {}, layerr = {}, pkid = {}, pkquote = {}, value = {}'.format(layerc.name(), layerr.name(), pkid, pkquote, value))


    f = QgsFeature(layerc.fields())
    try:
        e = dicto["data"]["attributes"]
    except:
        e = dicto["data"][0]["attributes"]

    for ff in f.fields().names(): logI ('layerc fieldnames {}'.format(ff))    
    # Copy attributes from dict to feature
    for k, v in e.items():
        if k == "temaattributter":
            for k2, v2 in v.items():
                logI ('TemaAttributter: ' + k2 + '~ ' + str(v2))
                f.setAttribute(k2, v2)
        elif k == "shape":
            f.setGeometry(cnvGJ2QgsGeometry(v))
        else:
            logI ('Attributter: ' + k + '~ ' + str(v))
            f.setAttribute(k, v)

    f.setAttribute(pkid,value)

    # set filter to find update object
    expression = '"{0}"={2}{1}{2}'.format(pkid,value,pkquote)
    logI ('Expression = ' + expression)

    # Update current layer
    layerc.startEditing()
    for g in layerc.getFeatures(QgsFeatureRequest().setFilterExpression(expression)): 
        g.setGeometry(f.geometry())      
        for ff in f.fields().names(): 
            logI ('layerc ff = {}, f[ff] = {}'.format(ff, f[ff]))
            g.setAttribute(ff, f[ff])  
        gr = g
        layerc.updateFeature(g)
    layerc.commitChanges()

    # Update reference layer
    layerr.startEditing()
    i = 0 
    for g in layerr.getFeatures(QgsFeatureRequest().setFilterExpression(expression)):
        i += 1
        g.setGeometry(f.geometry())      
        for ff in f.fields().names(): 
            logI ('layerr ff = {}, f[ff] = {}'.format(ff, f[ff]))
            g.setAttribute(ff, f[ff])  
        layerr.updateFeature(g)
    layerr.commitChanges()

    if i == 0: 
        logI('Insert...')
        layerr.dataProvider().addFeatures([gr])

def loadLayer(layer, dicto):
    """Converts an object dictionary to a list of features"""
    j = 0
    for fi in layer.fields():
        # logI(' Field no: {} : {}'.format(j, fi.name()))
        j += 1

    # Iterate object and create features
    layer.startEditing()
    j = 0

    for d in dicto["data"]:
        j += 1
        f = QgsFeature(layer.fields())
        e = d["attributes"]

        for k, v in e.items():
            if k == "temaattributter":
                for k2, v2 in v.items():
                    f.setAttribute(k2, v2)
            elif k == "shape":
                f.setGeometry(cnvGJ2QgsGeometry(v))
                #logI('GEOMETRI .... k={}, v={}, geometry = {}'.format(k, v, f.geometry().asWkt()))

            else:
                f.setAttribute(k, v)

        layer.addFeatures([f])

    layer.updateExtents()
    # logI('No of features: {} {}'.format(j, layer.featureCount()))
    layer.commitChanges()

    return layer


def cnvGJ2QgsGeometry(gjgd):
    """TBD"""

    gtype = gjgd["type"].lower()
    gc = gjgd["coordinates"]

    if gtype == 'point':
        qgeom = QgsGeometry.fromPointXY(gc[0], gc[1])

    elif gtype == 'linestring':
        qgeom = QgsGeometry.fromPolylineXY(fArr2QgsPointArr(gc))

    elif gtype == 'polygon':
        ma = []
        for g in gc:
            ma.append(fArr2QgsPointArr(g))
        qgeom = QgsGeometry.fromPolygonXY(ma)

    elif gtype == 'multipoint':
        qgeom = QgsGeometry.fromMultiPointXY(fArr2QgsPointArr(gc))

    elif gtype == 'multilinestring':
        ma = []
        for g in gc:
            ma.append(fArr2QgsPointArr(g))
        qgeom = QgsGeometry.fromMultiPolylineXY(ma)

    elif gtype == 'multipolygon':
        ma = []
        for g in gc:
            mb = []
            for h in g:
                mb.append(fArr2QgsPointArr(h))
            ma.append(mb)
        qgeom = QgsGeometry.fromMultiPolygonXY(ma)

    else:
        qgeom = None

    return qgeom


def fArr2QgsPointArr(flist):
    """TBD"""
    qpl = []
    for f in flist:
        qpl.append(QgsPointXY(f[0], f[1]))

    return qpl


def addLayer2Tree(tree, layer, tb, vname=None, vvalue=None, style=None, tname=None):
    """Replace with explanation"""

    ltl, l2 = findLayerVariableValue(vname, vvalue)

    if l2 is None:

        if tb:
            ltl = tree.insertLayer(0, layer)
        else:
            ltl = tree.addLayer(layer)

        QgsProject.instance().addMapLayer(layer, False)

        if style:
            logI('Style = {}'.format(style))
            layer.loadNamedStyle(style)

        if tname:
            ltl.setName(tname)

        assignLayerVariable(layer, vname, vvalue)

        layer.triggerRepaint()

    return ltl


def copyLayer2Layer(lyr, udict, owrite):

    contype = udict['contype']
    options = {}
    if owrite == True: options['overwrite'] = True

    if  contype == 'ogr':

        options['update'] = True
        options['layerName'] = udict['tname']
        uristr = udict['uri']
        options['driverName'] = 'gpkg'
        logI('uristr='+uristr)
        err = QgsVectorLayerExporter.exportLayer(lyr, uristr, "ogr", lyr.crs(), False, options)
        uristr += '|layername={}'.format(udict['tname'])
        logI('uri='+uristr)
        logI('options='+options['driverName'])

    else:

        uri = udict['uri']
        uri.setTable(udict['tname'])
        if 'gname' in udict and udict['gname'] != '': uri.setGeometryColumn(udict['gname'])
        #if udict['pkname'] != '': uri.setKeyColumn(udict['pkname'])

        uristr = uri.uri()
        err = QgsVectorLayerExporter.exportLayer(lyr, uristr, contype, lyr.crs(), False, options)


    if err[0] != QgsVectorLayerExporter.NoError:
        logW('Import layer {} failed with error {}'.format(lyr.name(), err))
        return None
    else:
        logI('Layer {} : {} : import ok'.format(lyr.name(),uristr))
        return QgsVectorLayer(uristr, lyr.name(),contype)
        

def loadVectorTableFromConnection (connection, schema, table, layername): 

    urlstr = connection.tableUri(schema, table)
    
    tableprm = connection.table(schema, table)
    pkidlst = tableprm.primaryKeyColumns() 
    geomstr = tableprm.geometryColumn()

    uri = QgsDataSourceUri(urlstr)

    if connection.providerKey() != 'ogr': 
        uri.setKeyColumn(pkidlst[0])
        uri.setGeometryColumn(geomstr)

    logI('*'+uri.uri())
    logI(connection.providerKey())
    if connection.providerKey() != 'ogr':
        layer = QgsVectorLayer(uri.uri(), layername, connection.providerKey())
    else:

        layer = QgsVectorLayer(uri.uri().replace("'","").replace("/","\\"),layername, connection.providerKey())

    return layer

