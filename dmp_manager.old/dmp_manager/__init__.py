# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DMPManager
                                 A QGIS plugin
 Manage data from Danmarmarks Miljøportal (DMP)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-08
        copyright            : (C) 2020 by Bo Victor Thomsen, AestasGIS Danmark 
        email                : bvt@aestas.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DMPManager class from file DMPManager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .dmp_manager import DMPManager
    return DMPManager(iface)