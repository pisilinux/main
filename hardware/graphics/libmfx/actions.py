 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --with-libva_drm=yes \
                         --with-libva_x11=yes \
                         ")    
    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS","LICENSE", "README.md")