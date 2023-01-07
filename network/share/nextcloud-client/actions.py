#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/-fPIE/-fPIC/g' src/{gui,cmd}/CMakeLists.txt")

    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=None \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed' \
                          -DNO_SHIBBOLETH=1 \
                          -DWITH_CRASHREPORTER=OFF \
                          -DUNIT_TESTING=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README.md")

    # Pisi Linux does not have Cinnamon Desktop yet.
    # pisitools.removeDir("/usr/share/nemo-python")
