#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DUSE_SYSTEM_XZ=ON \
                          -DUSE_SYSTEM_SQUASHFUSE=ON \
                          -DUSE_SYSTEM_LIBARCHIVE=ON \
                          -DUSE_SYSTEM_BOOST=ON \
                          -DUSE_SYSTEM_XDGUTILS=ON \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
