#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("source")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DENABLE_STATIC=OFF")

def build():
    shelltools.cd("source")
    cmaketools.make()

def install():
    shelltools.cd("source")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/libx265.a")

