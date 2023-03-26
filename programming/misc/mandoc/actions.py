#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed('configure', '"/usr/local"', '"/usr"')
    pisitools.dosed('configure', '"${PREFIX}/man"', '"${PREFIX}/share/man"')
    autotools.configure("MANDIR=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s MANDIR=/usr/share/man" % get.installDIR())

    # man-db
    pisitools.remove("/usr/bin/soelim")
    pisitools.remove("/usr/bin/apropos")
    pisitools.remove("/usr/bin/whatis")
    pisitools.remove("/usr/bin/man")

    pisitools.remove("/usr/share/man/man1/man.1")
    pisitools.remove("/usr/share/man/man1/whatis.1")
    pisitools.remove("/usr/share/man/man7/man.7")
    pisitools.remove("/usr/share/man/man1/apropos.1")

    pisitools.dodoc("LICENSE", "TODO", "NEWS")
