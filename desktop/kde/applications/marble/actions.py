#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DWITH_libshp=OFF \
                    -DWITH_libgps=OFF \
                    -DWITH_QextSerialPort=OFF \
                    -DWITH_liblocation=OFF \
                    -DBUILD_MARBLE_TOOLS=YES \
                    -DBUILD_TESTING=OFF \
                    -DBUILD_MARBLE_EXAMPLES=OFF \
                    -DBUILD_MARBLE_TESTS=OFF \
                    -DMOBILE=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("BUGS", "ChangeLog", "CODING", "COPYING*", "CREDITS", "LICENSES/*", "MANIFESTO.txt", "USECASES")
