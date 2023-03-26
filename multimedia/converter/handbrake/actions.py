#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

J = ''.join([
    ' --prefix=/usr',
    ' --disable-rpath',
    ' --disable-gtk4',
    ' --disable-silent-rules',
    ' --disable-update-checks',
    ' --enable-x265',
    ' --enable-qsv',
    ' --enable-numa',
    ' --enable-fdk-aac '
    ])

def setup():
	shelltools.export("CXXFLAGS", get.CXXFLAGS())
	shelltools.export("CFLAGS", get.CFLAGS())
	shelltools.cd("gtk")
	autotools.autoreconf("-fiv")
	shelltools.cd("..")
	autotools.rawConfigure("--force %s" % J)

def build():
	autotools.make("-C build")

def install():
	autotools.rawInstall("-C build DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("*.markdown", "COPYING", "LICENSE")
