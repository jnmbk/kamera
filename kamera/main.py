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

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from wizard import Wizard
import kamera_rc

def main():
    app = QApplication(sys.argv)

    app.setApplicationName("kamera")
    app.setOrganizationName("kamera")

    locale = QLocale.system().name()
    translator = QTranslator()
    translator.load(":/kamera_%s.qm" % locale)
    app.installTranslator(translator)

    wizard = Wizard()
    wizard.show()

    return app.exec_()

if __name__ == "__main__":
    main()
