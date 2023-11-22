#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

# shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))
# shelltools.export("LDFLAGS", "%s -Wl,--as-needed" % get.LDFLAGS())

def setup():
    mesontools.configure("-Dlibmpv=true \
                                        -Dcdda=enabled \
                                        -Ddvdnav=enabled \
                                        -Dsdl2=enabled \
                                        -Ddvbin=enabled \
                                        -Dlibarchive=enabled")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.insinto("/usr/share/mpv/scripts", "TOOLS/lua/*")

    pisitools.dodoc("Copyright", "RELEASE_NOTES", "README.md")
