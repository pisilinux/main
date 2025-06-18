#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import get

def setup():
    shelltools.system("rm -f po/de/docs/kstars/index.docbook")
    shelltools.system("sed -e 's|DATA_INSTALL_DIR|CMAKE_INSTALL_DATADIR|g' -i kstars/data/*/CMakeLists.txt")
    kde6.configure("-DBUILD_QT5=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*", "ChangeLog", "README*")
