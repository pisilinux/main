#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    # Disable jumbo build https://bugreports.qt.io/browse/QTBUG-88657 gcc10
    shelltools.system("sed -i 's|use_jumbo_build=true|use_jumbo_build=false|' -i src/buildtools/config/common.pri")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    #shelltools.export("QT5LINK", "/usr/lib/qt5/bin")
    #shelltools.export("QT5DIR", "/usr/lib/qt5")
    #shelltools.export("CFLAGS", "%s -I/usr/lib/sqlite3.16.2" % get.CFLAGS())
    #shelltools.system("qmake WEBENGINE_CONFIG+=use_proprietary_codecs WEBENGINE_CONFIG+=use_system_icu WEBENGINE_CONFIG+=use_system_protobuf WEBENGINE_CONFIG+=use_system_ffmpeg qtwebengine.pro")
    #pisitools.ldflags.add("-Wl,--no-keep-memory ")
    #shelltools.export("NINJAJOBS", "-j 4")
    shelltools.system("qmake .. -- -proprietary-codecs \
                   -system-ffmpeg \
                   -system-opus \
                   -system-webp \
                   -spellchecker \
                   -webengine-icu \
                   -webengine-kerberos")
    
def build():
    shelltools.cd("build")
    qt5.make()

def install():
    shelltools.cd("build")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
       #pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)
    
    shelltools.cd("..")
    pisitools.dodoc("LICENSE*")
