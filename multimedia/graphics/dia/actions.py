#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --with-python',
    ' --with-swig',
    ' --disable-nls',
    ' --disable-gnome',
    ' --disable-static '
    ' --disable-hardbooks',
    ])

def setup():
	#pisitools.dosed("Makefile.in", "samples po sheets", "samples sheets")
	autotools.configure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.removeDir("/usr/share/man/fr")

	pisitools.dodoc("AUTHORS", "MAINTAINERS", "NEWS", "THANKS")
