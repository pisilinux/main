#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap")
    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/GeoIP", "GeoIP-data/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
