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
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DEXIV2_ENABLE_VIDEO=yes \
                          -DEXIV2_ENABLE_WEBREADY=yes \
                          -DEXIV2_ENABLE_CURL=yes \
                          -DEXIV2_ENABLE_NLS=ON \
                          -DEXIV2_BUILD_SAMPLES=no")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README*", "doc/ChangeLog")
