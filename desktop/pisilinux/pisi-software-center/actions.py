#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("cargo build --release ")

    
def install():
	shelltools.system("cargo install --path . --root='%s'/usr" % get.installDIR())
	pisitools.insinto("/usr/share/applications/", "assets/pisi-software-center.desktop")
	pisitools.insinto("/usr/share/applications/pisi/", "assets/pisi-installer.desktop")
	pisitools.insinto("/usr/share/mime/packages/", "assets/pisi-mime.xml")
	pisitools.insinto("/usr/share/icons/", "assets/pisi-software-center.png")
	pisitools.remove("/usr/.crates.toml")
	pisitools.remove("/usr/.crates2.json")
	pisitools.dodoc("LICENSE", "README.md","TODO.md*")