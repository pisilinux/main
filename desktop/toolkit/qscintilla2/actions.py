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

WorkDir = "QScintilla_gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.cd("Qt4Qt5")
    shelltools.system("qmake qscintilla.pro")

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4Qt5/")
    shelltools.system("qmake-qt5 designer.pro INCLUDEPATH+=../Qt4Qt5 QMAKE_LIBDIR+=../Qt4Qt5")

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

def build():
    shelltools.system("cp -rf Python Python3")
    shelltools.cd("Qt4Qt5")
    qt5.make()

    shelltools.cd("../designer-Qt4Qt5/")
    qt5.make()

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
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    shelltools.cd("../designer-Qt4Qt5/")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #build and install qscintilla-python
    shelltools.cd("../Python3")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #pisitools.insinto("/usr/lib/python3.6/site-packages/PyQt5", "Qsci.so")
    shelltools.cd("../Python")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #pisitools.insinto("/usr/lib/python2.7/site-packages/PyQt5", "Qsci.so")

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4Qt5/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    pisitools.dodoc("LICENSE*", "NEWS", "README")
