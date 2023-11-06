#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde5.configure("-DPHONON_BUILD_QT5=OFF \
                              -DPHONON_BUILD_SETTINGS=OFF \
                              -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON")

def build():
    kde5.make()

def install():
    kde5.install()
    
    # Conflicts with qt5-phonon
    pisitools.removeDir("/usr/share")
