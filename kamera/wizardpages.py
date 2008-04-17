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

from PyQt4.QtGui import *
import ui_intro, ui_nowebcamfound

Page_Intro, Page_NoWebcamFound = range(2)

class IntroPage (QWizardPage, ui_intro.Ui_Form):
    def initializePage(self):
        self.setTitle(QApplication.translate("IntroPage", "About Wizard"))
        self.setupUi(self)

    def nextId(self):
        #collect devices from usb
        import usblist
        devices = usblist.getList()

        #check if they exist in db
        import database
        db = database.Database()
        driversFound = False
        for device in devices:
            device.drivers = db.get_driver_for_device_id(device.id)
            if device.drivers:
                driversFound = True
                for driver in device.drivers:
                    print "Found:", driver["description"] ,"for", device.description, "in", driver["driver"]
        if driversFound:
            return Page_Intro
        else:
            return Page_NoWebcamFound

class NoWebcamFoundPage (QWizardPage, ui_nowebcamfound.Ui_Form):
    def initializePage(self):
        self.setTitle(QApplication.translate("NoWebcamFoundPage", "No Webcams Found"))
        self.setupUi(self)
