#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
	pisitools.cflags.add("-Wno-deprecated-declarations")
	pisitools.unlink("*.stamp")
	autotools.autoreconf("-fv")
	autotools.configure("--enable-gtk3 --disable-buildin-polkit --disable-buildin-clipboard")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

