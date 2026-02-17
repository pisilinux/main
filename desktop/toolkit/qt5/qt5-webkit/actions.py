#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i '16i#include <cstdint>' Source/ThirdParty/woff2/include/woff2/output.h")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DUSE_LIBHYPHEN=OFF \
                          -DPORT=Qt \
                          -DENABLE_XSLT=OFF \
                          -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
                          -DENABLE_TOOLS=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        #pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)
    
    shelltools.cd("..")
    pisitools.dodoc("LICENSE*")
