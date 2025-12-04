# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get, pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


# WorkDir="pyside-setup-everywhere-src-%s/sources/shiboken6" % get.srcVERSION()

def setup():
    shelltools.cd("sources/shiboken6")
    pisitools.dosed("libshiboken/CMakeLists.txt", 'LIBRARY DESTINATION "shiboken6"', 'LIBRARY DESTINATION "${LIB_INSTALL_DIR}"')
    cmaketools.configure("-B build -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=OFF \
                          -DSHIBOKEN_PYTHON_LIBRARIES=`pkgconf python3-embed --libs` \
                          -DUSE_PYTHON_VERSION=3")


def build():
    shelltools.cd("sources/shiboken6/build")
    cmaketools.make()

def install():
    shelltools.cd("sources/shiboken6/build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    # pisitools.removeDir("/usr/shiboken6")

    # pisitools.dosed("%s/usr/lib/cmake/Shiboken6/Shiboken6Targets-release.cmake" % get.installDIR(), "/shiboken6/", "/lib/")
