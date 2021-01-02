#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
	pisitools.dosed("libindicator/Makefile.am", "-Werror", "")
	pisitools.dosed("tools/Makefile.am", "-Werror", "")
	autotools.autoreconf("-fiv")
	autotools.configure("--with-gtk=3 --disable-tests --disable-static --disable-deprecations")
	# fix autotypo.
	pisitools.dosed("libindicator/Makefile", "-lglib-2.0-lm", "-lglib-2.0 -lm")
	pisitools.dosed("tools/Makefile", "-lglib-2.0-lm", "-lglib-2.0 -lm")

	pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS")

