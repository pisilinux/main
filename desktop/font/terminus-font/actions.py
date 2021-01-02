#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	pisitools.dosed("75-yes-terminus.conf", "Term", "xos4 Term")
	autotools.configure("--x11dir=/usr/share/fonts/misc --otbdir=/usr/share/fonts/misc --psfdir=/usr/share/kbd/consolefonts")

def build():
	autotools.make("all otb")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.insinto("/etc/fonts/conf.avail", "75-yes-terminus.conf", "75-yes-terminus.conf")
	for t in shelltools.ls("*.otb"):
		pisitools.insinto("/usr/share/fonts/misc", t)
	pisitools.dosym("../conf.avail/75-yes-terminus.conf", "/etc/fonts/conf.d/75-yes-terminus.conf")

	pisitools.dodoc("AUTHORS", "CHANGES", "README")

