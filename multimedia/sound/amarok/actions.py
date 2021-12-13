#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("XDG_DATA_DIRS", get.workDIR())

def setup():
    #shelltools.system("sed -i -e 's|PATH_SUFFIXES lastfm5|PATH_SUFFIXES lastfm|' cmake/modules/FindLibLastFm.cmake")
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DLIB_INSTALL_DIR=lib \
                    -DPLUGIN_INSTALL_DIR=/usr/lib/qt5/plugins \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DBUILD_TESTING=OFF \
                    -DKDE_DISTRIBUTION_TEXT='PisiLinux'")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("AUTHORS", "README", "COPYING*", "ChangeLog")
