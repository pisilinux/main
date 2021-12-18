#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

WorkDir = "."

def setup():
	pass

def build():
	autotools.make("-C lexilla/src")
	autotools.make("-C scintilla/gtk")
	autotools.make("-C scite/gtk prefix=/usr")

def install():
	autotools.make("-C scite/gtk DESTDIR=%s install" % get.installDIR())

	pisitools.dosym("/usr/bin/SciTE", "/usr/bin/scite")
