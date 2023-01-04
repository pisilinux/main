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

	shelltools.cd("OpenCL-Headers-2021.06.30")
	cmaketools.configure("-DCMAKE_BUILD_TYPE=Release")

	shelltools.cd("../OpenCL-CLHPP-2.0.15")
	cmaketools.configure("-DBUILD_EXAMPLES=OFF -DBUILD_TESTS=OFF")

def build():
	autotools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("NEWS")

	shelltools.cd("OpenCL-Headers-2021.06.30")
	cmaketools.install()

	shelltools.cd("../OpenCL-CLHPP-2.0.15")
	cmaketools.install()
