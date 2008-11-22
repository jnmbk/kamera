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

import os, shutil, sys
from distutils.core import setup
from distutils.command.build import build
from distutils.command.clean import clean

PRJ = "kamera"
PRJM = __import__(PRJ)

try:
    import PyQt4
except:
    print "\033[31mWarning: You have to install PyQt4 on your system\033[0m"

def compileui(path, uiFile):
    compiled = os.system("pyuic4 %s%s.ui -o %s/ui_%s.py" % (path, uiFile, PRJ, uiFile))
    if compiled == 0:
        print "Compiled %s%s.ui -> %s/ui_%s.py" % (path, uiFile, PRJ, uiFile)
    else:
        print "\033[31mWarning: Failed compiling %s%s.ui, pyuic4 didn't work\033[0m" % (path, uiFile)

def compileqrc(path, qrcFile):
    compiled = os.system("pyrcc4 %s%s.qrc -o %s/%s_rc.py" % (path, qrcFile, PRJ, qrcFile))
    if compiled == 0:
        print "Compiled %s%s.qrc -> %s/%s_rc.py" % (path, qrcFile, PRJ, qrcFile)
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
            for file in os.listdir(PRJ):
                if file[-4:] == ".pyc":
                    os.remove(os.path.join(PRJ, file))
            print "removed *.pyc"
        except:pass

class myBuild(build):
    def run(self):
        build.run(self)
        try:
            uiFiles = [("ui/", file[:-3]) for file in os.listdir("ui")]
            for ui in uiFiles:
                if not ui[1] in (".", ".."):
                    compileui(ui[0], ui[1])
        except TypeError:
            print "No .ui files to compile"
        if os.system("lrelease-qt4 data/%s_tr_TR.ts -qm data/%s_tr_TR.qm" % (PRJ, PRJ)) == 0:
            print "Compiled data/%s_tr_TR.ts -> data/%s_tr_TR.qm" % (PRJ, PRJ)
        else:
            print "\033[31mWarning: Failed compiling data/%s_tr_TR.ts, lrelease-qt4 didn't work\033[0m" % PRJ
        for qrc in (("data/", PRJ),):
            compileqrc(qrc[0], qrc[1])

datas = [('share/applications', ['data/%s.desktop' % PRJ])]

setup(name = PRJ,
      version = PRJM.__version__,
      description = "webcam photographer",
      author = "Ugur Cetin",
      author_email = "ugur.jnmbk@gmail.com",
      license = "GNU General Public License, Version 3",
      url = "http://kamera.googlecode.com/",
      packages = [PRJ],
      data_files = datas,
      scripts = ['data/%s' % PRJ],
      cmdclass = {"build" : myBuild,
                  "clean" : myClean}
      )
