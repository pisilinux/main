#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("export SONAME_LIBVULKAN=lvulkan-1")
    options = "--disable-doxygen-doc \
                --prefix=/usr \
                --with-spirv-tools \
                --enable-static=no \
              "

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("LDFLAGS", "%s -L/usr/lib32"  % get.LDFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

        options += " --libdir=/usr/lib32 \
                     --includedir=/_emul32/include \
                     --bindir=/_emul32/bin \
                  "

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/_emul32")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "_usr", "usr")
        return

    pisitools.dodoc("AUTHORS", "LICENSE", "COPYING", "README")
