# -*- coding: utf-8 -*-
from json import load, dump, dumps, loads
import requests
from PyQt5.QtCore import QCoreApplication, Qt, QDateTime, QPointF, QVariant
from PyQt5.QtGui import QPolygonF
from qgis.utils import iface
from qgis.core import QgsMessageLog, Qgis, QgsVectorLayer, QgsProject, \
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsGeometry, \
    QgsField, QgsExpressionContextUtils, QgsFeature, QgsPointXY

trClassName = ''


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

    for ltLayer in QgsProject.instance().layerTreeRoot().findLayers():
        if evalue == QgsExpressionContextUtils.layerScope(ltLayer.layer()).variable(ename):
            return ltLayer, ltLayer.layer()

    return None, None


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


def createGroup(groupName, root):
    """TBD"""

    group = root.findGroup(groupName)

    if group is None:
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
        i = gobj.transform(xform)
        return gobj


def cnvobj2wkt(gobj, epsg_in, epsg_out):
    """Replace with explanation"""

    return cnvobj2obj(gobj, epsg_in, epsg_out).asWkt()


def cnvwkt2obj(wkt, epsg_in, epsg_out):
    """Replace with explanation"""

    return cnvobj2obj(QgsGeometry.fromWkt(wkt), epsg_in, epsg_out)


def cnvwkt2wkt(wkt, epsg_in, epsg_out):
    """Replace with explanation"""

    return cnvobj2wkt(QgsGeometry.fromWkt(wkt), epsg_in, epsg_out)


def wkbtype2simple(wtype):
    """Replace with explanation"""

    my_WkbType = {0: 'pnt', 1: 'pnt', 2: 'lin', 3: 'pol', 4: 'pnt', 5: 'lin', 6: 'pol'}
    return my_WkbType[wtype]


def wkbtype2str(wtype):
    """Replace with explanation"""

    my_WkbType = {0: 'Unknown', 1: 'Point', 2: 'LineString', 3: 'Polygon', 4: 'MultiPoint', 5: 'MultiLineString', 6: 'MultiPolygon', 100: 'NoGeometry'}
    return my_WkbType[wtype]


def read_config(filename):
    """Replace with explanation"""

    file = open(filename)
    dictF = load(file)
    file.close()
    return dictF


def write_config(filename, config):  # functionality not tested; 2019-11-09
    """Replace with explanation"""

    file = open(filename, mode='w', encoding='utf8')
    dump(config, file, indent=4)
    file.close()


def handleRequest(url, isPost=False, headers=None, package=None, loglayer=None, module=''):
    """TBD"""

    if isPost:
        if headers:
            r = requests.post(url, json=package, headers=headers)\
                if package else requests.post(url, headers=headers)
        else:
            r = requests.post(url, json=package)\
                if package else requests.post(url)
    else:
        r = requests.get(url, headers=headers)\
            if headers else requests.get(url)

    scode = r.status_code
    dictR = r.json() if r.status_code == 200 else None

    if loglayer:

        stime = QDateTime.currentDateTime().toString(Qt.ISODate)

        feat = QgsFeature(loglayer.fields())
        feat['operation'] = 'post' if isPost else 'get'
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
                            '{}_{}'.format(temanr, createDateTimeName(tname)), 'memory')

        pr = vl.dataProvider()

        fl1, ll1 = createFieldListAttributter(dicta["attributter"])
        pr.addAttributes(fl1)

        fl2, ll2 = createFieldListTemaAttributter(dicta["temaattributter"], temanr)
        pr.addAttributes(fl2)

        vl.updateFields()

        return vl, ll1 + ll2

    # Error, temakode not found
    messC('Error creating memory layer, temanr: {} not found'.format(temanr))
    return None, None


def createFieldListAttributter(dictaa):
    """TBD"""

    fl = []
    ll = []

    for d in dictaa:

        if d["id"] != 'temaattributter':

            f, le = createField(d["attributes"])
            fl.append(f)
            if le:
                ll.append(le)

    return fl, ll


def createFieldListTemaAttributter(dictata, temanr):
    """TBD"""

    fl = []
    ll = []

    for d in dictata:

        if d["relationships"]["temakode"]["data"]["id"] == str(temanr):

            f, le = createField(d["attributes"])
            fl.append(f)
            if le:
                ll.append(le)

    return fl, ll


def createField(e):
    """TBD"""

    f = QgsField()
    le = None

    f.setName(e["name"])
    f.setAlias(e["title"])

    if e["default"]:
        f.setDefaultValueDefinition(e["default"])

    if e["data-type"] == "string":
        f.setType(QVariant.String)

    elif e['data-type'] == "uuid":
        f.setType(QVariant.String)
        f.setLength(36)

    elif e['data-type'] == "datetime":
        f.setType(QVariant.String)
        f.setLength(33)

    elif e['data-type'] == "number":
        f.setType(QVariant.Int)

    elif e['data-type'] == "domain":
        f.setType(QVariant.String)
        le = createMemLookup(e["domain"], e["name"])

    else:
        e.setType(QVariant.String)

    return f, le


def createMemLookup(domain, tfield):
    """TBD"""

    vl = QgsVectorLayer('None', createDateTimeName(tfield), 'memory')

    pr = vl.dataProvider()
    pr.addAttributes([QgsField("key", QVariant.String), QgsField("value", QVariant.String)])
    vl.updateFields()

    fetl = []
    for k, v in domain.items():
        fet = QgsFeature(vl.fields())
        fet.setAttributes([k, v])
        fetl.append(fet)
    pr.addFeatures(fetl)

    return vl


def loadLayer(layer, dicto):
    """Converts an object dictionary to a list of features"""
    j = 0
    for fi in layer.fields():
        logI(' Field no: {} : {}'.format(j, fi.name()))
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
                logI('GEOMETRI .... k={}, v={}, geometry = {}'.format(k, v, f.geometry().asWkt()))

            else:
                f.setAttribute(k, v)

        layer.addFeatures([f])

    layer.updateExtents()
    logI('No of features: {} {}'.format(j, layer.featureCount()))
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


def addLayer2Tree(tree, layer, tb, name=None, style=None):
    """Replace with explanation"""

    if tb:
        ltl = tree.insertLayer(0, layer)
    else:
        ltl = tree.addLayer(layer)

    QgsProject.instance().addMapLayer(layer, False)
    if style:
        layer.loadNamedStyle(style)

    layer.triggerRepaint()

    return ltl
