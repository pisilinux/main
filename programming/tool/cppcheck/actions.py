#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DHAVE_RULES=ON \
     -DBUILD_GUI=ON \
     -DWITH_QCHART=ON \
     -DENABLE_CHECK_INTERNAL=ON -L \
    "

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("-DUSE_Z3=OFF -DBUILD_TESTS=OFF %s" % j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

#def check():
#	cmaketools.make("test")

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../COPYING", "../readme*")

