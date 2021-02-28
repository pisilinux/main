#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))
shelltools.export("LDFLAGS", "%s -Wl,--as-needed" % get.LDFLAGS())

def setup():
    shelltools.system("./bootstrap.py")
    shelltools.system("python3 waf configure --prefix=/usr \
                                            --confdir=/etc/mpv \
                                            --enable-dvb \
                                            --enable-cdda \
                                            --enable-dvdnav \
                                            --enable-libarchive \
                                            --enable-libmpv-shared")

def build():
    shelltools.system("python3 waf build -v")

def install():
    shelltools.system("DESTDIR=%s python3 waf install" % get.installDIR())
    pisitools.insinto("/usr/share/mpv/scripts", "TOOLS/lua/*")

    pisitools.dodoc("Copyright", "RELEASE_NOTES", "README.md")
