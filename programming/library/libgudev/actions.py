#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
	autotools.configure("--prefix=/usr \
                        --enable-introspection \
                        --enable-gtk-doc \
                        --disable-umockdev")
	
	if get.buildTYPE() == "_emul32" :
		
		shelltools.export("CC", "gcc -m32")
		shelltools.export("CXX", "g++ -m32")
		shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
		
		autotools.configure("--prefix=/usr \
							 --libdir=/usr/lib32 \
                             --disable-introspection \
                             --disable-gtk-doc \
                             --disable-umockdev")
    
	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("AUTHORS", "COPYING")
