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

from PyQt4.QtCore import QSettings, QVariant
from PyQt4.QtSql import QSqlDatabase, QSqlQuery

from defaultsettings import DATABASE_FILE_LOCATION

class Database:
    def __init__(self):
        settings = QSettings()
        self.database = QSqlDatabase.database()
        if not self.database.isValid():
            self.database = QSqlDatabase.addDatabase("QSQLITE")
            self.database.setDatabaseName(
                    str(
                        settings.value(
                            "database/fileLocation",
                            DATABASE_FILE_LOCATION).toString()
                        )
                    )
            self.database.open()

    def get_driver_for_device_id(self, device_id):
        query = QSqlQuery()
        results = []
        query.prepare(
                "select package_name, version, description from drivers join devices "
                "where usb_id=:device_id and drivers.ROWID=devices.driver_id"
                )
        query.bindValue(":device_id", QVariant(device_id))
        query.exec_()

        while query.next():
            results.append({
                    "driver" : query.value(0).toString(),
                    "version" : query.value(1).toString(),
                    "description" : query.value(2).toString(),
                    })
        return results
