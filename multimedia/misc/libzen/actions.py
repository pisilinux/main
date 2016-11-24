#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "ZenLib/Project/GNU/Library"

def setup():
    libtools.libtoolize("--automake")
    autotools.aclocal()
    autotools.automake("-afc")
    autotools.autoconf()
    autotools.configure("--disable-static --enable-shared")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosed("libzen.pc", "^(Version:).*", r"\1 %s" % get.srcVERSION())
    pisitools.dosed("libzen.pc", "^Libs_Static.*$")
    pisitools.dodir("/usr/lib/pkgconfig")
    pisitools.insinto("/usr/lib/pkgconfig", "libzen.pc")
    shelltools.cd("../../../")
    pisitools.dodoc("*.txt")
    shelltools.cd("Source/ZenLib")
    pisitools.dodir("/usr/include/ZenLib")
    pisitools.insinto("/usr/include/ZenLib", "*.h")
    for it in ["HTTP_Client", "Format/Html", "Format/Http"]:
        pisitools.dodir("/usr/include/ZenLib/%s" % it)
        pisitools.insinto("/usr/include/ZenLib/%s" % it, "%s/*.h" % it)
