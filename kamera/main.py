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

import sys

from PyQt4.QtGui import *

def main():
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.show()

    return app.exec_()

if __name__ == "__main__":
    main()
