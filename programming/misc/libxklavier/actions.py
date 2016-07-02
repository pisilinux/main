#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
                        --with-xkb-bin-base=/usr/bin \
                        --with-xkb-base=/usr/share/X11/xkb \
                        --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("NEWS", "README", "CREDITS", "AUTHORS", "ChangeLog")
