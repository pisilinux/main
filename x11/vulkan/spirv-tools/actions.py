#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

pisitools.cxxflags.add("-std=gnu++11")

def setup():
  
	shelltools.system("mv SPIRV-Headers-1.5.1.corrected external/SPIRV-Headers")
	
	if get.buildTYPE() == "emul32":
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib32 \
						      -DBUILD_SHARED_LIBS=ON \
						      -DSPIRV_WERROR=Off \
						      -DSKIP_SPIRV_TOOLS_INSTALL=OFF \
						      -DCMAKE_INSTALL_BINDIR=bin32")
	else:
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
						      -DBUILD_SHARED_LIBS=ON \
						      -DSPIRV_WERROR=Off")
    

def build():
	cmaketools.make()
    

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())
	if get.buildTYPE() == "emul32":
		pisitools.removeDir("/usr/bin32")
	

	pisitools.dodoc("LICENSE", "README.md", "CONTRIBUTING.md")
