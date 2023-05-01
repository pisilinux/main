#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
    -DMZ_PROJECT_SUFFIX='-ng' \
    -DMZ_ZSTD=OFF \
    -DBUILD_SHARED_LIBS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/include/zip.h")
    pisitools.remove("/usr/include/unzip.h")

    pisitools.dodoc("LICENSE", "README*")
