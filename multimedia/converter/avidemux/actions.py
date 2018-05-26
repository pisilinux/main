#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("bash ./bootStrap.bash")

def install():
    autotools.install()

    pisitools.insinto("/", "install/usr")
    pisitools.dobin("install/usr/lib/libADM*", "/usr/lib")
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    pisitools.dodoc("COPYING", "AUTHORS", "License*")
    pisitools.doman("man/*")
