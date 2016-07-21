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
    shelltools.system("qmake-qt5 qscintilla.pro")

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
    pythonmodules.run("configure.py -n ../Qt4Qt5 -o ../Qt4Qt5")
    autotools.make()

    shelltools.cd("../Python3")
    pythonmodules.run("configure.py -n ../Qt4Qt5 -o ../Qt4Qt5", pyVer = "3")
    pisitools.dosed("Makefile", "-lpython3.4", "-lpython3")
    autotools.make()

def install():
    shelltools.cd("Qt4Qt5")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    shelltools.cd("../designer-Qt4Qt5/")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #build and install qscintilla-python
    shelltools.cd("../Python3")
<<<<<<< HEAD
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/python3.4/site-packages/PyQt5", "Qsci.so")
    shelltools.cd("../Python")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/python2.7/site-packages/PyQt5", "Qsci.so")
=======
    autotools.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../Python")
    autotools.install("DESTDIR=%s" % get.installDIR())
>>>>>>> remotes/origin/revert-679-master

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4Qt5/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

<<<<<<< HEAD
=======
    pisitools.removeDir("/usr/share/qt4")

>>>>>>> remotes/origin/revert-679-master
    pisitools.dodoc("LICENSE*", "NEWS", "README")

# By PiSiDo 2.3.1
