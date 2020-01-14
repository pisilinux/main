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

ver = get.srcVERSION()

def setup():
	cmaketools.configure("-DCMAKE_INSTALL_SYSCONFDIR=/etc \
		                  -DCMAKE_SKIP_RPATH=True \
		                  -DBUILD_WSI_XCB_SUPPORT=On \
						  -DBUILD_WSI_XLIB_SUPPORT=On \
						  -DBUILD_WSI_WAYLAND_SUPPORT=On \
						  -DBUILD_CUBE=ON \
						  -DBUILD_VULKANINFO=ON \
						  -DBUILD_ICD=OFF \
						  ")
    

def build():
	cmaketools.make()
    

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())  

    
	pisitools.dodoc("README.md", "CONTRIBUTING.md", "LICENSE.txt", "CODE_OF_CONDUCT.md", "GOVERNANCE.md")
