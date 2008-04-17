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

import usblist
import database

class DeviceManager:
    driversFound = False
    devices = []

    def __init__(self):
        self.refreshDeviceList()

    def refreshDeviceList(self):
        #collect devices from usb
        self.devices = usblist.getList()

        #check if they exist in db
        db = database.Database()
        for device in self.devices:
            device.drivers = db.get_driver_for_device_id(device.id)
            if device.drivers:
                self.driversFound = True
                for driver in device.drivers:
                    print "Found:", driver["description"] ,"for", device.description, "in", driver["driver"]
