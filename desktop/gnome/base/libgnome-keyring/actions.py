#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    shelltools.system("sed -i 's:"'/desktop:'"/org:' " + get.curDIR() + "/schema/*.xml")

    mesontools.configure("-Dselinux=disabled \
                          -Dsystemd=disabled")


def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dosym("/usr/lib/security/pam_gnome_keyring.so", "/lib/security/pam_gnome_keyring.so")

    pisitools.dodoc("NEWS", "README*", "COPYING")
