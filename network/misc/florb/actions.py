#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_BUILD_TYPE=RelWithDebInfo \
     -DCMAKE_INSTALL_PREFIX=/usr -L \
    "

def setup():
	pisitools.flags.add("-pthread -lXpm")
	pisitools.unlinkDir("src/i18n/de_DE")
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	pisitools.dobin("build/src/florb")
	pisitools.dopixmaps("src/res/florb.png")
	shelltools.chmod("src/res/florb.svg", mode = 0644)
	pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "src/res/florb.svg")

#	pisitools.dodoc("LICENSE.txt", "README.txt")

