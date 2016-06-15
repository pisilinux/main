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
    shelltools.export("QT5LINK", "/usr/lib/qt5/bin")
    shelltools.export("QT5DIR", "/usr/lib/qt5")
    shelltools.export("CFLAGS", "%s -I/usr/lib/sqlite3.11.0.0" % get.CFLAGS())
    qt5.configure(parameters="WEBENGINE_CONFIG+=use_proprietary_codecs")
    #shelltools.system("qmake-qt5 WEBENGINE_CONFIG+=use_proprietary_codecs qtwebengine.pro")
    
    
def build():
    qt5.make()
    #Drop QMAKE_PRL_BUILD_DIR because reference the build dir
    #shelltools.system('find "$pkgdir/usr/lib" -type f -name '*.prl' -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;')

def install():
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
       pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    pisitools.dodoc("LICENSE.LGPLv3")
