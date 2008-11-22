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

import os

from PyQt4 import QtCore
from PyQt4 import QtGui

from opencvwidget import OpenCVWidget, CamThread
from ui_mainwindow import Ui_MainWindow

class MyOpenCVWidget(OpenCVWidget):
    def __init__(self, label):
        self.imageLabel = label
        self.camThread = CamThread()
        self.connect(self.camThread, QtCore.SIGNAL("image"), self.updateImage)
        self.camThread.start()

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.settings = QtCore.QSettings()
        self.createImageList()
        self.opencvwidget = MyOpenCVWidget(self.label_webcam)

    @QtCore.pyqtSignature("bool")
    def on_pushButton_save_clicked(self):
        fileextension = self.settings.value("image/format", QtCore.QVariant("png")).toString()
        filename = "kamera_%s.%s" % (QtCore.QDateTime.currentDateTime().toString("yyyyMMdd-hhmmss"), fileextension)
        self.opencvwidget.snapShot().save(filename)
        self.addImage(self.opencvwidget.pixmap)

    def createImageList(self):
        self.imageFiles = [file for file in os.listdir(".") if file.startswith("kamera_")]
        imageLayout = QtGui.QHBoxLayout()
        self.imageListWidget = QtGui.QWidget()
        self.imageListWidget.setLayout(imageLayout)
        for imageFile in self.imageFiles:
            self.addImage(QtGui.QPixmap(imageFile))
        self.scrollArea_photos.setWidget(self.imageListWidget)

    def addImage(self, pixmap):
        label = QtGui.QLabel(self.imageListWidget)
        label.setPixmap(pixmap.scaledToHeight(100))
        label.setMaximumSize(label.pixmap().size())
        label.setStyleSheet("border-right:2px solid gray;border-bottom:2px solid black")
        self.imageListWidget.layout().addWidget(label)
