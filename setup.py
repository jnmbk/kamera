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

import os, shutil, sys
from distutils.core import setup
from distutils.command.build import build
from distutils.command.clean import clean

import kamera

try:
    import PyQt4
except:
    print "\033[31mWarning: You have to install PyQt4 on your system\033[0m"

def compileui(path, uiFile):
    compiled = os.system("pyuic4 %s%s.ui -o kamera/%s_ui.py" % (path, uiFile, uiFile))
    if compiled == 0:
        print "Compiled %s%s.ui -> kamera/%s_ui.py" % (path, uiFile, uiFile)
    else:
        print "\033[31mWarning: Failed compiling %s%s.ui, pyuic4 didn't work\033[0m" % (path, uiFile)

def compileqrc(path, qrcFile):
    compiled = os.system("pyrcc4 %s%s.qrc -o kamera/%s_rc.py" % (path, qrcFile, qrcFile))
    if compiled == 0:
        print "Compiled %s%s.qrc -> kamera/%s_rc.py" % (path, qrcFile, qrcFile)
    else:
        print "\033[31mWarning: Failed compiling %s%s.qrc, pyrcc4 didn't work\033[0m" % (path, qrcFile)

class myClean(clean):
    def run(self):
        clean.run(self)
        try:
            os.remove("MANIFEST")
            print "removed MANIFEST"
        except:pass
        try:
            shutil.rmtree("build")
            print "removed build"
        except:pass
        try:
            for file in os.listdir("kamera"):
                if file[-4:] == ".pyc":
                    os.remove(os.path.join("kamera", file))
            print "removed *.pyc"
        except:pass

class myBuild(build):
    def run(self):
        build.run(self)
        try:
            uiFiles = [("ui/", file[:-3]) for file in os.listdir("ui")[1:]]
            for ui in uiFiles:
                compileui(ui[0], ui[1])
        except TypeError:
            print "No .ui files to compile"
        if os.system("lrelease-qt4 data/kamera_tr_TR.ts -qm data/kamera_tr_TR.qm") == 0:
            print "Compiled data/kamera_tr_TR.ts -> data/kamera_tr_TR.qm"
        else:
            print "\033[31mWarning: Failed compiling data/kamera_tr_TR.ts, lrelease-qt4 didn't work\033[0m"
        for qrc in (("data/", "kamera"),):
            compileqrc(qrc[0], qrc[1])

datas = [('share/applications', ['data/kamera.desktop'])]

setup(name = "kamera",
      version = kamera.__version__,
      description = "Easy webcam installer for Pardus",
      author = "Ugur Cetin",
      author_email = "ugur.jnmbk@gmail.com",
      license = "GNU General Public License, Version 2",
      url = "http://code.google.com/p/kamera/",
      packages = ["kamera"],
      data_files = datas,
      scripts = ['data/kamera'],
      cmdclass = {"build" : myBuild,
                  "clean" : myClean}
      )
