#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Imaging-%s" % get.srcVERSION()
# fix unused direct dependency warning
shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")

def install():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-incompatible-pointer-types -Wno-unused-but-set-variable -Wno-int-to-pointer-cast")
    #pisitools.dosed("_imagingft.c", "<freetype/freetype.h>", "<freetype2/freetype.h>")
    #pisitools.dosed("_imagingft.c", "<freetype/fterrors.h>", "<freetype2/fterrors.h>")
    pythonmodules.install()

    shelltools.cd("Sane")
    pythonmodules.install()
    shelltools.cd("..")

    for header in ["Imaging.h","ImPlatform.h"]:
        pisitools.insinto("/usr/include/%s" % get.curPYTHON(), "libImaging/%s" % header)

    pisitools.dodoc("README")