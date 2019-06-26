#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DWITH_DBUS=ON \
                          -DCMAKE_BUILD_TYPE=Release")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/inkscape/*.a")
    
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
