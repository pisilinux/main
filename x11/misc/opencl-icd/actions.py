 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	pisitools.insinto("/usr/include/CL", "OpenCL-Headers-2.1/CL/*")
	shelltools.export("CFLAGS", "-I%s/usr/include -O2")
	shelltools.export("CXXFLAGS", "-I%s/usr/include -O2")
	
	autotools.autoreconf("-vfi")
    
	autotools.configure()    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("COPYING","NEWS", "README")