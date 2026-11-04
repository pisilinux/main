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


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
	shelltools.export("CFLAGS", "-I%s/usr/include -O2")
	shelltools.export("CXXFLAGS", "-I%s/usr/include -O2")
	pisitools.cflags.add("-fcommon")
	shelltools.system("./bootstrap")

	autotools.configure()

	shelltools.cd("OpenCL-Headers-2026.05.29")
	cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
										-DCMAKE_INSTALL_DATADIR=%s" % Libdir)

	shelltools.cd("../OpenCL-CLHPP-2026.05.29")
	cmaketools.configure("-DBUILD_EXAMPLES=OFF \
										-DCMAKE_INSTALL_DATADIR=%s \
										-DOpenCLHeaders_DIR=%s/ocl-icd-%s/OpenCL-Headers-2026.05.29/OpenCLHeaders \
										-DBUILD_TESTING=OFF" % (Libdir, get.workDIR(), get.srcVERSION()))

def build():
	autotools.make()

	shelltools.cd("OpenCL-Headers-2026.05.29")
	cmaketools.make()

	shelltools.cd("../OpenCL-CLHPP-2026.05.29")
	cmaketools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("NEWS")

	shelltools.cd("OpenCL-Headers-2026.05.29")
	cmaketools.install()

	shelltools.cd("../OpenCL-CLHPP-2026.05.29")
	cmaketools.install()
