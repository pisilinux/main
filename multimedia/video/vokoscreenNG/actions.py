#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

WorkDir = "vokoscreenNG-%s/src" % get.srcVERSION()

def setup():
	pisitools.cxxflags.add("-Wno-deprecated-declarations")
	qt5.configure()

def build():
	qt5.make()

def install():
	pisitools.dobin("vokoscreenNG")
	pisitools.insinto("/usr/share/applications", "applications/vokoscreenNG.desktop", "vokoscreenNG.desktop")
	pisitools.insinto("/usr/share/pixmaps", "applications/vokoscreenNG.png", "vokoscreenNG.png")

	pisitools.dodoc("../COPYING", "../README.md")

