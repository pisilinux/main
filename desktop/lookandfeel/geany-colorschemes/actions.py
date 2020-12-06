#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools, shelltools, get

def install():
	pisitools.insinto("/usr/share/geany/colorschemes", "colorschemes/*")
	for t in shelltools.ls("%s/usr/share/geany/colorschemes/*" % get.installDIR()):
		shelltools.chmod(t, mode = 0644)

	pisitools.dodoc("ADDING-A-THEME.md", "AUTHORS", "COPYING", "README.md")

