#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
                            
	cmaketools.configure("-DEXIV2_BUILD_PO=ON \
		                  -DEXIV2_BUILD_SAMPLES=OFF \
		                  -DEXIV2_ENABLE_VIDEO=ON \
		                  -DCMAKE_INSTALL_LIBDIR=lib \
		                  ")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "README.md")
