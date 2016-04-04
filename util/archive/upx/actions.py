#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("UPX_LZMA_VERSION", "0x465")
    shelltools.export("UPX_LZMADIR", get.workDIR())

def build():
    autotools.make("all")

def install():
    pisitools.insinto("/usr/bin", "src/upx.out", "upx")
    pisitools.insinto("/usr/share/man/man1", "doc/upx.1")
    pisitools.dodoc("BUGS", "COPYING", "LICENSE", "NEWS", "PROJECTS", "README*", "THANKS" )
