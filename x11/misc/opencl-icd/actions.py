#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.export("CFLAGS", "-I%s/usr/include -O2")
	shelltools.export("CXXFLAGS", "-I%s/usr/include -O2")
	pisitools.cflags.add("-fcommon")
	shelltools.system("./bootstrap")

	autotools.configure()

	shelltools.cd("OpenCL-Headers-2023.04.17")
	cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
										-DCMAKE_INSTALL_DATADIR=/usr/lib")

	shelltools.cd("../OpenCL-CLHPP-2023.04.17")
	cmaketools.configure("-DBUILD_EXAMPLES=OFF \
										-DCMAKE_INSTALL_DATADIR=/usr/lib \
										-DBUILD_TESTING=OFF")

def build():
	autotools.make()

	shelltools.cd("OpenCL-Headers-2023.04.17")
	cmaketools.make()

	shelltools.cd("../OpenCL-CLHPP-2023.04.17")
	cmaketools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("NEWS")

	shelltools.cd("OpenCL-Headers-2023.04.17")
	cmaketools.install()

	shelltools.cd("../OpenCL-CLHPP-2023.04.17")
	cmaketools.install()
