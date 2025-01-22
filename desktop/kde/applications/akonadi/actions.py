#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    kde6.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE \
                    -DMYSQLD_EXECUTABLE:FILEPATH=/usr/bin/mysqld \
                    -DWITH_SOPRANO=OFF")

def build():
    kde6.make()

def install():
    kde6.install()
    pisitools.dodoc("AUTHORS", "NEWS", "README.md")
