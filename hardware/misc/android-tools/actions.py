#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DANDROID_TOOLS_LIBUSB_ENABLE_UDEV=ON \
                          -DANDROID_TOOLS_USE_BUNDLED_LIBUSB=ON", sourceDir="..")

def build():
    cmaketools.make("-C build")
    #cmaketools.make("-C build doc")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
