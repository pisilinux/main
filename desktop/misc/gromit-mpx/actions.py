#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	cmaketools.configure("-Bbuild -DCMAKE_INSTALL_SYSCONFDIR=/etc -L")

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../ChangeLog", "../NEWS.md", "../README.md")

