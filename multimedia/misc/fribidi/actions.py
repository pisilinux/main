#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

def setup():
    autotools.autoreconf("-fiv")
    options = "--disable-static --with-pic"

    if get.buildTYPE()=="emul32":
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += "--libdir=/usr/lib32"

    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # unneeded empty manpages.
    pisitools.removeDir("/usr/share/man")

    if get.buildTYPE()=="emul32":
        pisitools.dodoc("AUTHORS", "NEWS", "THANKS")
