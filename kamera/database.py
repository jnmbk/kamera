#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v2
# Copyright 2008, Ugur Cetin
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from pysqlite2 import dbapi2 as sqlite
from PyQt4.QtCore import QSettings

from defaultsettings import DATABASE_FILE_LOCATION

class Database:
    def __init__(self):
        settings = QSettings()
        self.connection = sqlite.connect(str(settings.value("database/fileLocation",
            DATABASE_FILE_LOCATION).toString()))
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def get_driver_for_device_id(self, device_id):
        self.cursor.execute(
                "select package_name, version, description from drivers join devices "
                "where usb_id=? and drivers.driver_id=devices.driver_id", (device_id,))
        return self.cursor.fetchall()
