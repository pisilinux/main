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
    ' --with-mesa',
    ' --disable-debug',
    ' --enable-man',
    ' --enable-html',
    ' --enable-shared',
    ' --enable-threadsafe',
    ' --enable-exceptions',
    ' --enable-optimization',
    ' --enable-system-expat',
    ' --enable-javascript-api',
    ' --disable-maintainer-mode',
    ' --disable-dependency-tracking '
    ])

def setup():
    autotools.configure(i)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "THANKS")
