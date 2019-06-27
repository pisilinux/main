#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


WorkDir="x265_3.0"

def setup():
	
	shelltools.system("mkdir build8 build10 build12")
	
    #shelltools.cd("source")
    #cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          #-DENABLE_STATIC=OFF")

def build():
    #shelltools.cd("source")
    
    
	shelltools.cd("build12")
	shelltools.system("cmake ../source -G 'Unix Makefiles' \
		               -DCMAKE_INSTALL_PREFIX='/usr'\
		               -DHIGH_BIT_DEPTH='TRUE' \
		               -DMAIN12='TRUE' \
		               -DEXPORT_C_API='FALSE' \
		               -DENABLE_CLI='FALSE'\
		               -DENABLE_SHARED='FALSE' \
					  ")    
	cmaketools.make()
    
	shelltools.cd("../build10")
    
	shelltools.system("cmake ../source -G 'Unix Makefiles' \
		               -DCMAKE_INSTALL_PREFIX='/usr'\
		               -DHIGH_BIT_DEPTH='TRUE' \
		               -DEXPORT_C_API='FALSE' \
		               -DENABLE_CLI='FALSE'\
		               -DENABLE_SHARED='FALSE' \
					  ") 
	cmaketools.make()
	
	shelltools.cd("../build8")
	
	shelltools.system("ln -s ../build10/libx265.a libx265_main10.a")
	shelltools.system("ln -s ../build12/libx265.a libx265_main12.a")
	
	shelltools.system("cmake ../source -G 'Unix Makefiles' \
		               -DCMAKE_INSTALL_PREFIX='/usr' \
		               -DENABLE_SHARED='TRUE' \
		               -DENABLE_HDR10_PLUS='TRUE' \
		               -DEXTRA_LIB='x265_main10.a;x265_main12.a' \
		               -DEXTRA_LINK_FLAGS='-L.' \
		               -DLINKED_10BIT='TRUE' \
		               -DLINKED_12BIT='TRUE' \
					  ")
	cmaketools.make()
	
		               
	

def install():
    shelltools.cd("build8")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/libx265.a")

