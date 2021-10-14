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
    ' --disable-static',
    ' --disable-rpath',
    ' --disable-silent-rules',
    ' --enable-qsv',
    ' --enable-x265',
    ' --enable-numa',
    ' --enable-fdk-aac',
    ' --enable-libav-aac '
    ])

def setup():
	shelltools.export("CXXFLAGS", get.CXXFLAGS())
	shelltools.export("CFLAGS", get.CFLAGS())
	shelltools.cd("gtk")
	autotools.autoreconf("-fiv")
	shelltools.cd("..")
	autotools.rawConfigure("--prefix=/usr --force %s" % i)

def build():
	shelltools.cd("build")
	autotools.make()

def install():
	shelltools.cd("build")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../*.markdown", "../COPYING", "../LICENSE")

