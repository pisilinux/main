# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get, pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


# WorkDir="pyside-setup-everywhere-src-%s/sources/pyside6" % get.srcVERSION()

def setup():
    shelltools.cd("sources/pyside6")
    pisitools.dosed("libpyside/CMakeLists.txt", 'LIBRARY DESTINATION "PySide6"', 'LIBRARY DESTINATION "${LIB_INSTALL_DIR}"')
    pisitools.dosed("libpysideqml/CMakeLists.txt", 'LIBRARY DESTINATION "PySide6"', 'LIBRARY DESTINATION "${LIB_INSTALL_DIR}"')
    pisitools.dosed("CMakeLists.txt", '/wheels/cmake/PySide6', '/cmake/PySide6')
    cmaketools.configure("-B build -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=OFF \
                          -DSHIBOKEN_PYTHON_LIBRARIES=`pkgconf python3-embed --libs` \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3")


def build():
    shelltools.cd("sources/pyside6/build")
    cmaketools.make()


def install():
    shelltools.cd("sources/pyside6/build")
    # shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
