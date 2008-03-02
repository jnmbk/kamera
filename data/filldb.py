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

def gspcaList():
    devices = []
    for line in open("drivers/gspca.txt").readlines()[1:]:
        devices.append(
                (
                    2, # driver_id
                    "%s:%s" % ( # device_id
                        line[line.find('0x') + 2:][:4],
                        line[line.find('0x', line.find('0x') + 1) + 2:][:4]
                        ),
                    line[line.rfind("/*") + 3:line.rfind("*/") - 1] # description
                    )
                )
    return devices

con = sqlite.connect("webcams.db")
cur = con.cursor()

cur.executemany("insert into devices(driver_id, usb_id, description) values(?,?,?)", tuple(gspcaList()))
con.commit()
con.close()
