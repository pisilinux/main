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
    cmaketools.configure("-Bbuild -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=ON \
                          -DPRESENTATION_BACKEND=xlib \
                          -DDYNAMIC_LOADER=ON")

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build") 
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("CHANGELOG*", "BUILDING*", "LICENSE", "README*")
