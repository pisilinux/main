#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip=["/usr/lib"]

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s INSTALL_PREFIX=/usr" % get.installDIR())
	pisitools.insinto("/usr/bin", "wrapper/vmafossexec")
	pisitools.dodoc("CHANGELOG.md", "LICENSE", "NOTICE.md", "FAQ.md", "README.md")

