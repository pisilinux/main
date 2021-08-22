#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -e '/extern int efi_set_verbose/d' -i src/efibootmgr.c")

    shelltools.export("CFLAGS", "-Os")
    autotools.make("EFIDIR=pisilinux EFI_LOADER=grubx64.efi")

def install():
    shelltools.makedirs("%s/usr/sbin" % get.installDIR())
    shelltools.makedirs("%s/usr/share/man" % get.installDIR())
    shelltools.makedirs("%s/usr/include" % get.installDIR())
    
    autotools.rawInstall("EFIDIR=pisilinux DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/man", "src/*.8")
    pisitools.insinto("/usr/include", "src/include/*.h")
