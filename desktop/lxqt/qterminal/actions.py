#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

def setup():
    shelltools.system("qmake qterminal.pro")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                                        -DCMAKE_BUILD_TYPE=Release \
                                        -DPULL_TRANSLATIONS=no", sourceDir="..")
def build():
    shelltools.cd("build")
    qt5.make()

def install():
    shelltools.cd("build")
    qt5.install()
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS")
