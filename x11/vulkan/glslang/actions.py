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
  
	if get.buildTYPE() == "emul32":
		cmaketools.configure("-Bbuild-shared -DCMAKE_INSTALL_PREFIX='/usr' \
							  -DCMAKE_INSTALL_LIBDIR='lib32' \
			                  -DBUILD_SHARED_LIBS='ON' \
							  -DCMAKE_INSTALL_BINDIR=bin32 \
			                  -DALLOW_EXTERNAL_SPIRV_TOOLS='ON'")
			                  # -DENABLE_GLSLANG_BINARIES=OFF
	else:
		cmaketools.configure("-Bbuild-shared -DCMAKE_INSTALL_PREFIX='/usr' \
							  -DCMAKE_INSTALL_LIBDIR='lib' \
							  -DALLOW_EXTERNAL_SPIRV_TOOLS='ON' \
			                  -DBUILD_SHARED_LIBS='ON'")
    

def build():
	shelltools.cd("build-shared")
	cmaketools.make()
    

def install():
	shelltools.cd("build-shared")
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())

	if get.buildTYPE() == "emul32":
		pisitools.removeDir("/usr/bin32")
		for f in shelltools.ls("%s/usr/lib32/cmake" % get.installDIR()):
			pisitools.dosed("%s/usr/lib32/cmake/%s" % (get.installDIR(), f), "bin32", "bin")
	
	#for tool in ["glslangValidator", "spirv-remap"]:
		#pisitools.domove("/usr/bin32/%s" %tool, "/usr/bin", "%s-32" %tool)

    
    #pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt")
