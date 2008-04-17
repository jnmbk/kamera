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
from devicemanager import DeviceManager
import ui_intro, ui_nowebcamfound, ui_webcamlist

Page_Intro, Page_NoWebcamFound, Page_WebcamList = range(3)

class IntroPage (QWizardPage, ui_intro.Ui_Form):
    deviceManager = None

    def initializePage(self):
        self.setTitle(QApplication.translate("IntroPage", "About Wizard"))
        self.setupUi(self)

    def nextId(self):
        if not self.deviceManager:
            self.deviceManager = DeviceManager()
        if self.deviceManager.driversFound:
            return Page_WebcamList
        else:
            return Page_NoWebcamFound

class NoWebcamFoundPage (QWizardPage, ui_nowebcamfound.Ui_Form):
    def initializePage(self):
        self.setTitle(QApplication.translate("NoWebcamFoundPage", "No Webcams Found"))
        self.setupUi(self)

class WebcamListPage (QWizardPage, ui_webcamlist.Ui_Form):
    def initializePage(self):
        self.setTitle(QApplication.translate("WebcamListPage", "Webcams Found"))
        self.setupUi(self)
