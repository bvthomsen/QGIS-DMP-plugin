# -*- coding: utf-8 -*-
from PyQt5.QtCore import QCoreApplication, Qt,  QDateTime
from qgis.utils import iface
from qgis.core  import QgsMessageLog, Qgis, QgsVectorLayer, QgsProject, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsGeometry, QgsWkbTypes, QgsField, QgsExpressionContextUtils, QgsFeature
from json import load, loads, dump, dumps
import requests

trClassName= ''

def trInit(message):

    global trClassName
    trClassName = message

# noinspection PyMethodMayBeStatic
def tr(message):

    global trClassName
    return QCoreApplication.translate(trClassName, message)

def findLayerVariableValue (ename, evalue):

    for layer in QgsProject.instance().layerTreeRoot().findLayers():
        if evalue == QgsExpressionContextUtils.layerScope(layer.layer()).variable(ename): return layer.layer()

    return None


def logI (mess,tab=None):

    global trClassName
    
    QgsMessageLog.logMessage(mess, tab or trClassName, Qgis.Info)

def logW (mess,tab=None):

    global trClassName
    QgsMessageLog.logMessage(mess, tab or trClassName, Qgis.Warning)

def logC (mess,tab=None):

    global trClassName
    QgsMessageLog.logMessage(mess, tab or trClassName, Qgis.Critical)

def messI (mess1,mess2,duration=5):

    global trClassName
    iface.messageBar().pushMessage (mess1 or trClassName, mess2, Qgis.Info, duration)
    iface.mainWindow().repaint()

def messW (mess1,mess2,duration=20):

    global trClassName
    iface.messageBar().pushMessage (mess1 or trClassName, mess2, Qgis.Warning, duration)
    iface.mainWindow().repaint()

def messC (mess1,mess2,duration=30):

    global trClassName
    iface.messageBar().pushMessage (mess1 or trClassName, mess2, Qgis.Critical,duration)
    iface.mainWindow().repaint()

def xstr(s):

    return '' if s is None else str(s)


def addMemoryLayer2tree (type, epsg, name, style, attr, tree, tb):

    epsgPrt = '' if epsg is None else "?crs=epsg:" + str(epsg).upper().replace('EPSG:','')
     
    vl = QgsVectorLayer(wkbtype2str(type)+epsgPrt, name , "memory")
    vl.dataProvider().addAttributes(attr)
    vl.updateFields()

    if tb:
        n = tree.insertLayer(0,vl)
    else:
        n = tree.addLayer(vl)

    QgsProject.instance().addMapLayer(vl, False)
    vl.loadNamedStyle(style)
    vl.triggerRepaint()

    return vl


def removeGroup(groupName, root):

    group = root.findGroup(groupName)
    if group is not None:
        root.removeChildNode(group)

def removeGroupLayer(groupName,layer, root):

    group = root.findGroup(groupName)
    if group is not None:
        # Find layer if exists
        ln = group.findLayer (layer)
        if layer is not None:
            group.removeChildNode(ln)

def clearGroupLayer(groupName,layer, root):

    group = root.findGroup(groupName)
    if group is not None:
        ln = group.findLayer (layer)
        if ln is not None:
            ln.layer().dataProvider.truncate()
            return ln

    return None


def cnvobj2obj (gobj,epsg_in,epsg_out):

    if epsg_in == epsg_out:
        return gobj

    else:
        crsSrc = QgsCoordinateReferenceSystem(epsg_in)
        crsDest = QgsCoordinateReferenceSystem(epsg_out)
        xform = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())
        i = gobj.transform(xform)
        return gobj

def cnvobj2wkt (gobj,epsg_in,epsg_out):

    return cnvobj2obj(gobj,epsg_in,epsg_out).asWkt()

def cnvwkt2obj (wkt,epsg_in,epsg_out):

    return cnvobj2obj(QgsGeometry.fromWkt(wkt),epsg_in,epsg_out)

def cnvwkt2wkt (wkt,epsg_in,epsg_out):

    return cnvobj2wkt(QgsGeometry.fromWkt(wkt),epsg_in,epsg_out)

def wkbtype2simple (type):

    my_WkbType = {0:'pnt', 1:'pnt', 2:'lin', 3:'pol', 4:'pnt', 5:'lin', 6:'pol'}
    return my_WkbType[type]

def wkbtype2str (type):

    my_WkbType = {0:'Unknown', 1:'Point', 2:'LineString', 3:'Polygon', 4:'MultiPoint', 5:'MultiLineString', 6:'MultiPolygon', 100:'NoGeometry'}
    return my_WkbType[type]

def is_http_url(s):
    return re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',s)


def read_config(filename):
    file = open(filename)
    dict = load(file)
    file.close()
    return dict

def write_config(filename, config):  # functionality not tested; 2019-11-09
    file = open(filename, mode='w', encoding='utf8')
    dump(config, file, indent=4)
    file.close()
    

def handleRequest (isPost,url,package=None,name='',loglayer=None):

    stime = QDateTime.currentDateTime().toString(Qt.ISODate) 
    
    if isPost:
        r = requests.post(url,json=package) if package else requests.post(url)
    else:
        r = requests.get(url) 

    scode = r.status_code
    dict = r.json() if r.status_code == 200 else None

    if loglayer:
        feat = QgsFeature(loglayer.fields())
        feat['operation'] = 'post' if isPost else 'get'
        feat['url'] = url
        feat['package'] = dumps(package, indent=2) if package else ''
        feat['status_code'] = str(scode)
        feat['dict'] = dumps(dict, indent=2)[:100000] if dict else ''
        feat['timestamp'] = stime 
        feat['module'] = name  
        loglayer.dataProvider().addFeatures ([feat])

    return scode, dict  

