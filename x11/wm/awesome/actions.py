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
    pisitools.cflags.add("-fcommon")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=RELEASE \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DSYSCONFDIR=/etc \
                          -DLUA_LIBRARY=/usr/lib/liblua.so \
                          -DLUA_INCLUDE_DIR=/usr/include", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.cd("..")
    #pisitools.dodoc("README* ")
