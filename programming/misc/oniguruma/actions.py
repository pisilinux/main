#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = ''.join([
    ' --prefix=/usr',
    ' --enable-posix-api',
    ' --enable-static=no',
    ' --disable-silent-rules '
    ])

def setup():
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING")
