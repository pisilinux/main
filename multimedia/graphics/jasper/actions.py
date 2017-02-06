#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr    \
                          -DCMAKE_INSTALL_LIBDIR=lib     \
                          -DCMAKE_BUILD_TYPE=Release     \
                          -DALLOW_IN_SOURCE_BUILD=ON     \
                          -DCMAKE_SKIP_INSTALL_RPATH=YES")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README")
