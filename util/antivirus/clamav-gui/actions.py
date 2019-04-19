#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


WorkDir = "ClamAV-GUI/"

def setup():
    shelltools.system("qmake -r PREFIX=/usr clamav-gui.pro")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
