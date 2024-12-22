#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
	# passed with --ignore-sandbox
	shelltools.cd("src")
	pisitools.dosed("fluid/dlg_search.fl", "Double\ resizable", "Double resizable modal")
	pisitools.dosed("OMakefile", "unroll-loops", "unroll-loops -fpermissive")
	for t in ["", "i18nupdate", "i18ncompile"]:
		shelltools.system("omake %s" % t)

def install():
	shelltools.cd("src")
	shelltools.system("omake PREFIX=%s/usr install" % get.installDIR())

	for mo in ["de_DE/LC_MESSAGES", "sv_SE/LC_MESSAGES"]:
		shelltools.chmod("%s/usr/share/locale/%s/florb.mo" % (get.installDIR(), mo), mode = 0644)

	for i in ["florb.xpm", "res/florb.png", "res/florb.svg"]:
		pisitools.insinto("/usr/share/pixmaps", i)

	pisitools.dodoc("../LICENSE.txt")
