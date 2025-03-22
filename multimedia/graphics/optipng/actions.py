#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

t = ''.join([
    ' --prefix=/usr',
    ' --mandir=/usr/share/man',
    ' --with-system-zlib',
    ' --with-system-libpng '
    ])

def setup():
    autotools.rawConfigure(t)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS.txt", "LICENSE.txt")
