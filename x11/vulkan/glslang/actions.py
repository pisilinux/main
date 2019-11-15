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
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib32 \
			                  -DBUILD_SHARED_LIBS=ON \
			                  -DENABLE_GLSLANG_BINARIES=OFF")
	else:
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
			                  -DBUILD_SHARED_LIBS=ON")
    

def build():
	cmaketools.make()
    

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())  
	
	#for tool in ["glslangValidator", "spirv-remap"]:
		#pisitools.domove("/usr/bin32/%s" %tool, "/usr/bin", "%s-32" %tool)

    
    #pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt")
