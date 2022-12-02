#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools

j = ''.join([
    ' -O3',
    ' -Wall',
    ' -D_GNU_SOURCE',
    ' -std=c99',
    ' -fvisibility=hidden',
    ' -fPIC',
    ' -fcommon '
    ])

def build():
	autotools.make("prefix=/usr CFLAGS='%s'" % j)

def install():
	pisitools.dobin("foma")
	pisitools.dobin("flookup")
	pisitools.dobin("cgflookup")
	pisitools.insinto("/usr/include", "fomalib.h")
	pisitools.insinto("/usr/include", "fomalibconf.h")
	pisitools.dolib_so("libfoma.so.0.9.18")
	pisitools.dosym("libfoma.so.0.9.18", "/usr/lib/libfoma.so")
	pisitools.dosym("libfoma.so.0.9.18", "/usr/lib/libfoma.so.0")
