#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

NoStrip = "/"

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "CXXFLAGS")
    qt5.configure()

def build():
    qt5.make()
    qt5.make("docs")

def install():
    #pisitools.insinto("/usr/lib/qt5/qml", "qml/QtQml")
    #pisitools.insinto("/usr/lib/qt5/qml", "qml/Qt")
    #pisitools.insinto("/usr/lib/qt5/qml", "qml/QtQuick")
    #pisitools.insinto("/usr/lib/qt5/qml", "qml/QtQuick.2")
    #pisitools.insinto("/usr/lib/qt5/qml", "qml/QtTest")        
    qt5.install("INSTALL_ROOT=%s install_docs" % get.installDIR())

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        #pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    pisitools.insinto("/usr/share/licenses/qt5-declarative/", "LICENSE*")
