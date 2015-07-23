#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_TESTS=OFF \
                          -DQCA_SUFFIX=qt5 \
                          -DQCA_INSTALL_IN_QT_PREFIX=ON", sourceDir="..")
 

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("README", "TODO", "COPYING")
    
    pisitools.domove("/usr/share/qt5/man/man1/qcatool-qt5.1", "/usr/share/man/man1/qcatool-qt5.1")
    pisitools.removeDir("/usr/share/qt5")
