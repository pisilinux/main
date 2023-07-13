#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
        -DMZ_LIB_SUFFIX='-ng' \
        -DBUILD_SHARED_LIBS=ON")

def build():
    # shelltools.system("cmake -B build -S minizip-4.0.0")
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/include/minizip/zip.h")
    pisitools.remove("/usr/include/minizip/unzip.h")

    pisitools.dodoc("LICENSE", "README*")
