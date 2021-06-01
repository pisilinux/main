#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's:"'/desktop:'"/org:' " + get.curDIR() + "/schema/*.xml")

    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --with-pam-dir=/lib/security \
                         --enable-valgrind")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "COPYING", "AUTHORS", "ChangeLog")
