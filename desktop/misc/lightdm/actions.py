#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
  #  shelltools.export("MOC5", "moc-qt5")

    autotools.configure("--prefix=/usr \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --libexecdir=/usr/libexec \
                         --disable-static \
                         --disable-tests \
                         --enable-liblightdm-qt5 \
                         --with-greeter-user=lightdm \
                         --with-greeter-session=pisi-lightdm-greeter")
    
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

