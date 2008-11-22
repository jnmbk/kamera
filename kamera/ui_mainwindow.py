# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Sat Nov 22 06:33:18 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(14, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtGui.QPushButton(self.widget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        spacerItem3 = QtGui.QSpacerItem(439, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea_photos = QtGui.QScrollArea(self.splitter)
        self.scrollArea_photos.setWidgetResizable(True)
        self.scrollArea_photos.setObjectName("scrollArea_photos")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea_photos)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 90))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_photos.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Getting video from webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

