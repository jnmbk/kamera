#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2008, Ugur Cetin
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import pisi
import usblist
import database

class DeviceManager:
    driversFound = False
    devices = []

    def refreshDeviceList(self):
        """
        Collects USB device list and adds driver list to device when found in database.
        You can reach them using DeviceManeger.devices
        """

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

    def webcamList(self):
        """ Returns a list of webcam devices which have drivers """
        webcams = []
        for device in self.devices:
            if device.drivers:
                webcams.append(device)
        return webcams

    def isDriverInstalled(self, driver, version=None):
        """ Returns True if given driver is installed """
        #TODO: check for version number
        pisi.api.init(write=False)
        installed = pisi.api.ctx.installdb.is_installed(driver)
        pisi.api.finalize()
        return installed
