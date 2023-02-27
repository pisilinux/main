#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' --bindir=/usr/local/bin',
    ' --includedir=/usr/include/iconv',
    ' --enable-extra-encodings',
    ' --disable-static '
    ])

def setup():
	autotools.configure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.remove("/usr/share/doc/*.html")
	pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "THANKS")
