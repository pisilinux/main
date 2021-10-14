#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("go generate -v")

def build():
	shelltools.system("go build -v")

def install():
	pisitools.dobin("ymuse")
	pisitools.insinto("/usr/share/applications", "resources/ymuse.desktop", "ymuse.desktop")
	shelltools.copy("resources/icons", "%s/%s/icons" % (get.installDIR(), get.dataDIR()))
	shelltools.copy("resources/i18n/generated", "%s/%s/locale" % (get.installDIR(), get.dataDIR()))

	pisitools.dodoc("COPYING", "README.md")

