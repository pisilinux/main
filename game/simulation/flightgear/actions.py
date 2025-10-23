#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|Exec=.*|Exec=fgfs --fg-root=/usr/share/flightgear/data|' package/org.flightgear.FlightGear.desktop.in")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                         -DCMAKE_INSTALL_LIBDIR=lib    \
                         -DCMAKE_INSTALL_DATADIR=/usr/share \
                         -DFG_DATA_DIR=/usr/share/flightgear")

def build():
    cmaketools.make()
    
def install():
    cmaketools.install()

    shelltools.copy("%s/usr/appdir/usr/share/*" % get.installDIR(), "%s/usr/share/" % get.installDIR())
    pisitools.removeDir("/usr/appdir")
    pisitools.dodoc("README*", "ChangeLog", "AUTHORS", "NEWS", "Thanks")
