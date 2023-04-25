#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --disable-native',
    ' --enable-jp2',
    ' --enable-cups',
    ' --enable-release',
    ' --with-opengl=yes',
    ' --with-xft',
    ' --disable-static '
    ])

def setup():
	pisitools.dosed("configure.ac", "-fno-stack-protector", "-fstack-protector-strong")
	pisitools.dosed("lib/FXRex.cpp", "#define\ TOPIC_REXDUMP", "// #define TOPIC_REXDUMP")
	autotools.autoreconf("-fiv")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "LICENSE_ADDENDUM", "README")
