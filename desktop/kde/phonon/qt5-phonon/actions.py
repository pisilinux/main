#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON \
                    -DPHONON_BUILD_PHONON4QT5=ON \
                    -D__KDE_HAVE_GCC_VISIBILITY=NO \
                    -DCMAKE_INSTALL_LIBDIR=lib")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dosym("/usr/include/KDE/Phonon", "/usr/include/Phonon")
