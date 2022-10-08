#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

#NoStrip = "/"

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

def setup():
    # shelltools.system("sed -i 's/python /python3 /' qtdeclarative.pro \
                                                    # src/3rdparty/masm/masm.pri")
    #shelltools.system("sed -i 's/python /python3 /' qtdeclarative/src/3rdparty/masm/masm.pri")
    # shelltools.export("CFLAGS", "CXXFLAGS")
    qt6.configure("-DQT_FEATURE_system_freetype=ON")

def build():
    qt6.make()
    #qt6.make("docs")

def install():
    #pisitools.insinto("/usr/lib/qt6/qml", "qml/QtQml")
    #pisitools.insinto("/usr/lib/qt6/qml", "qml/Qt")
    #pisitools.insinto("/usr/lib/qt6/qml", "qml/QtQuick")
    #pisitools.insinto("/usr/lib/qt6/qml", "qml/QtQuick.2")
    #pisitools.insinto("/usr/lib/qt6/qml", "qml/QtTest")
    qt6.install()

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    pisitools.insinto("/usr/share/licenses/qt6-declarative/", "LICENSE*")
