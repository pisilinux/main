#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("meson setup build \
        --prefix=/usr \
        -Ddefault-hvs=qemu,xen,lxc \
        -Dupdate-icon-cache=false \
        -Dcompile-schemas=false \
        -Dtests=disabled")

def build():
    shelltools.system("meson compile -C build")

def install():
    shelltools.system("meson install -C build --destdir %s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS.md", "README.md")
