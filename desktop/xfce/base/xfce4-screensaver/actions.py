#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

j = ''.join([
    '-Dsession-manager=elogind',
    ' -Dauthentication-scheme=pam',
    ' -Dshadow=true',
    ' -Dpam-auth-type=system'])

def setup():
#    shelltools.system("patch -Rp1 < 0001-Catch-gs_listener_dbus_init-failures.patch")
    mesontools.configure(j)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING*", "NEWS", "README.md")

