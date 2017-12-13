#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    shelltools.system("meson .. --prefix=/usr --sysconfdir=/etc --localstatedir=/var -Dsystemd=false -Dconsolekit=true -Dplugin_uefi_labels=false -Dplugin_thunderbolt=false -Dgtkdoc=false -Dman=false")

def build():
    shelltools.cd("build")
    
    shelltools.system("ninja")
    

def install():
    shelltools.cd("build")
    
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
