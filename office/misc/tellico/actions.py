#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde5


def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                              -DCMAKE_INSTALL_PREFIX=/usr \
                              -DWITH_Nepomuk=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
