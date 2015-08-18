#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -D__KDE_HAVE_GCC_VISIBILITY=NO \
                    -DPHONON_BUILD_PHONON4QT5=ON")

def build():
    kde5.make()

def install():
    kde5.install()
    
