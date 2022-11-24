#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
#	pisitools.dosed("gnome/libopenraw-gnome-0.3.pc.in", "1", "3")
	autotools.configure("--enable-gnome --disable-static")

def build():
	autotools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "NEWS", "RELEASE_NOTES")

