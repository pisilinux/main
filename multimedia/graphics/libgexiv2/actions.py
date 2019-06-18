#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("meson build --prefix=/usr -Dgtk_doc=true")

def build():
    shelltools.system("ninja -C build")

def install():
    shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
