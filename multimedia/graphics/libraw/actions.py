#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static --enable-jpeg --enable-jasper --enable-lcms")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/lib/libraw.so.23.0.0", "/usr/lib/libraw.so.20")
    pisitools.dosym("/usr/lib/libraw_r.so.23.0.0", "/usr/lib/libraw_r.so.20")

    pisitools.dodoc("README*")
