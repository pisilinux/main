#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_BUILD_TYPE=Release \
     -DENABLE_PHONON=ON \
     -DENABLE_MPV=ON \
     -DENABLE_VLC=OFF \
    "

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.install()

	pisitools.dodoc("../CHANGES.md", "../COPYING", "../README.md")

