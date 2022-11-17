#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools, get

WorkDir = "."

def install():
	for t in shelltools.ls("*.cvd"):
		pisitools.insinto("/var/lib/clamav", t)
		shelltools.chown("%s/var/lib/clamav/%s" % (get.installDIR(), t), uid = "clamav", gid = "clamav")
