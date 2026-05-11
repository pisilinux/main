#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' --disable-tests',
    ' --disable-{schemas-compile,nautilus-actions} '
    ])

def setup():
    shelltools.system("NOCONFIGURE=1 sh autogen.sh")
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.GPL3", "THANKS")
