#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import qt5

WorkDir = "QScintilla-gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.cd("Qt4Qt5")
    qt5.configure()

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4Qt5/")
    qt5.configure()

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

def build():
    shelltools.system("cp -rf Python Python3")
    shelltools.cd("Qt4Qt5")
    autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CXX()))

    shelltools.cd("../designer-Qt4Qt5/")
    autotools.make("DESTDIR=\"%s/%s/designer\"" % (get.installDIR(), qt5.plugindir))

    # Get Makefile of qscintilla-python via sip
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -n ../Qt4Qt5 -o ../Qt4Qt5 -c --pyqt=PyQt5 --pyqt-sipdir=/usr/share/sip/Py2Qt5 --qsci-sipdir=/usr/share/sip/Py2Qt5 --sip-incdir=/usr/lib/python2.7/site-packages --qmake /usr/bin/qmake-qt5")
    pisitools.dosed("Makefile", "/usr/include/qt/QtPrintSupport", "/usr/include/qt5/QtPrintSupport")
    pisitools.dosed("Makefile", "/usr/include/qt/QtWidgets", "/usr/include/qt5/QtWidgets")
    autotools.make()
    shelltools.cd("../Python3")
    pythonmodules.run("configure.py -n ../Qt4Qt5 -o ../Qt4Qt5 -c --pyqt=PyQt5 --qmake /usr/bin/qmake-qt5", pyVer = "3")
    pisitools.dosed("Makefile", "/usr/include/qt/QtPrintSupport", "/usr/include/qt5/QtPrintSupport")
    pisitools.dosed("Makefile", "/usr/include/qt/QtWidgets", "/usr/include/qt5/QtWidgets")
    autotools.make()

def install():
    shelltools.cd("Qt4Qt5")
    qt5.install()

    shelltools.cd("../designer-Qt4Qt5/")
    qt5.install()

    #build and install qscintilla-python
    shelltools.cd("../Python3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/python3.4/site-packages/PyQt5", "Qsci.so")
    shelltools.cd("../Python")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/python2.7/site-packages/PyQt5", "Qsci.so")

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4Qt5/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    #pisitools.removeDir("/usr/share/qt4")

    pisitools.dodoc("LICENSE*", "NEWS", "README")
