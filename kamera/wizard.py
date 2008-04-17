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

from wizardpages import *

class Wizard(QWizard):
    def __init__(self):
        QWizard.__init__(self)
        self.setWindowTitle("Kamera")
        self.setPage(Page_Intro, IntroPage())
        self.setPage(Page_NoWebcamFound, NoWebcamFoundPage())
