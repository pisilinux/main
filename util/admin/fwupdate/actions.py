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

# WorkDir = ""
# NoStrip = "/"

#def setup():
#    shelltools.system("sed 's@ -Werror\([[:space:]]\|\n\)@\1@' -i linux/Makefile")

def build():
    autotools.make("V=1 EFIDIR=org.pisilinux GNUEFIDIR=/usr/lib LIBDIR=/usr/lib")

def install():
    pisitools.dodir("/usr/include")
    autotools.rawInstall("LIBDIR=/usr/lib libexecdir=/usr/lib/ EFIDIR=org.pisilinux GNUEFIDIR=/usr/lib DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/boot/efi/EFI", "/usr/lib/fwupdate/EFI")
    pisitools.removeDir("/boot")
    pisitools.removeDir("/usr/lib/debug")
    pisitools.removeDir("/usr/src")
    pisitools.removeDir("/usr/share/fwupdate")
    

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
