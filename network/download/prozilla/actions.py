#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's/DL_Window:://' src/download_win.h")
    autotools.configure("--prefix=/usr \
                         --mandir=/usr/share/man \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dosym("/usr/bin/proz", "/usr/bin/prozilla")

    pisitools.dodoc("CREDITS", "COPYING*", "README")

