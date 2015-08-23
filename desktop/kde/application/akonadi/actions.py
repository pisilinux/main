#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE \
                    -DWITH_SOPRANO=OFF")

def build():
    kde5.make()

def install():
    kde5.install()
    pisitools.dodoc("AUTHORS", "NEWS", "README")
