#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' -DUSE_Z3=ON',
    ' -DHAVE_RULES=ON',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DBUILD_GUI=ON',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DBUILD_TESTS=OFF',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DUSE_BUNDLED_TINYXML2=OFF',
    ' -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON',
    ' -DENABLE_CHECK_INTERNAL=ON',
    ' -DWITH_QCHART=ON -L '
    ])

def setup():
	cmaketools.configure("-Bbuild %s" % j)

def build():
	shelltools.cd("build")
	cmaketools.make()

def check():
	pass

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS")
