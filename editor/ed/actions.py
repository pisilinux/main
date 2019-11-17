 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def setup():
	shelltools.system("bsdtar xf ed-1.15.tar.lz")
	
	shelltools.cd("ed-1.15")
	autotools.configure("--disable-static \
                         --enable-shared \
                         ")        

def build():
	shelltools.cd("ed-1.15")
	autotools.make()  

def install():
	shelltools.cd("ed-1.15")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS","COPYING", "README", "NEWS")