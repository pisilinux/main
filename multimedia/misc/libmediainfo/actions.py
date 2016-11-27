#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.cd("MediaInfoLib/Project/GNU/Library")
    libtools.libtoolize("--automake")
    autotools.aclocal()
    autotools.automake("-afc")
    autotools.autoconf()
    autotools.configure("--enable-shared \
                         --disable-static \
                         --with-libcurl \
                         --with-libmms")

def build():
    shelltools.cd("MediaInfoLib/Project/GNU/Library")
    autotools.make()

def install():
    shelltools.cd("MediaInfoLib/Project/GNU/Library")
    autotools.install()
    pisitools.dosed("libmediainfo.pc", "^(Version:)\s+$", r"\1 %s\n" % get.srcVERSION())
    pisitools.dosed("libmediainfo.pc", "^Libs_Static.*$", "")
    pisitools.dodir("/usr/lib/pkgconfig")
    pisitools.insinto("/usr/lib/pkgconfig", "libmediainfo.pc")
    shelltools.cd("../../../")
    pisitools.dodoc("*.txt")
    pisitools.dohtml("*.html")
    for it in ["MediaInfo", "MediaInfoDLL"]:
        pisitools.dodir("/usr/include/%s" % it)
        pisitools.insinto("/usr/include/%s" % it, "Source/%s/*.h" % it)


