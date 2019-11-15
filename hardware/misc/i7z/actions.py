 
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

#pisitools.flags.add("-I/opt/intel/mediasdk/include/ -L/opt/intel/mediasdk/bin/x64/ -lmfxhw64")

#def setup():
    #autotools.autoreconf("-vfi")
    #autotools.configure("--disable-static \
                         #--enable-shared \
                         #")    
    

def build():
    autotools.make()
    shelltools.cd("src/GUI")
    shelltools.system("qmake .")
    autotools.make()    

def install():
    pisitools.insinto("/usr/bin", "src/GUI/i7z_GUI", "i7z-gui")
    autotools.rawInstall("DESTDIR=%s sbindir=/usr/bin/ prefix=/usr" % get.installDIR())

    #pisitools.dodoc("AUTHORS","LICENSE", "README.md")