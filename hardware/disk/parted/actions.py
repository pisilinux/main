#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.autoconf()

    autotools.configure("--disable-rpath --disable-static --disable-gcc-warnings")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")

