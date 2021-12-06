#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")

    shelltools.system("""sed -i 's/libzmq_werror="yes"/libzmq_werror="no"/' configure""")
    shelltools.system("sed -i 's/openpgm-5.1/openpgm-5.2/' configure configure.ac")

    autotools.configure("--with-pgm --with-libsodium --disable-static")
    # fix unused dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include", "cppzmq-4.8.0/*.hpp")
