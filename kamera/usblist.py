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

import os

class UsbDevice:
    ''' represents a connected USB device '''
    bus = "000"
    device = "000"
    id = "0000:0000"
    description = "Generic USB device"
    def __str__(self):
        return "%s %s %s %s" % (self.bus, self.device, self.id, self.description)

def getList():
    ''' returns a list of devices connected to USB '''

    deviceList = []
    lsusb = os.popen("/usr/sbin/lsusb","r")
    for line in lsusb.readlines():
        device = UsbDevice()
        device.bus = line[4:7]
        device.device = line[15:18]
        device.id = line[23:32]
        device.description = line[33:]
        deviceList.append(device)
    lsusb.close()
    return deviceList
