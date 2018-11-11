#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#tools = ["sha1pass", "md5pass", "mkdiskimage*", "keytab-lilo", "syslinux2ansi", "lss16toppm","pxelinux-options"]
datadir = "/usr/lib/syslinux"

NoStrip = ["/sbin", "/usr/lib"]

def build():
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("LDFLAGS", "")
    # do not swallow efi compilation output to make debugging easier
    shelltools.system("sed 's|> /dev/null 2>&1||' -i efi/check-gnu-efi.sh")
      
    # disable debug and development flags to reduce bootloader size
    shelltools.system("truncate --size 0 mk/devel.mk")

    autotools.make("-j1 PYTHON=python bios efi64 efi32")

def install():
    autotools.rawInstall('INSTALLROOT=%s MANDIR="/usr/share/man" AUXDIR="/usr/lib/syslinux"' % get.installDIR())

    pisitools.removeDir("/usr/lib/syslinux/com32")
    pisitools.removeDir("/usr/lib/syslinux/dosutil")
    pisitools.remove("/usr/lib/syslinux/syslinux.com")
    
    pisitools.dodir("/usr/lib/syslinux/bios")
    
    pisitools.domove("/usr/lib/syslinux/*.c32", "/usr/lib/syslinux/bios")
    pisitools.domove("/usr/lib/syslinux/*.bin", "/usr/lib/syslinux/bios")
    pisitools.domove("/usr/lib/syslinux/*.0", "/usr/lib/syslinux/bios")
    pisitools.domove("/usr/lib/syslinux/memdisk", "/usr/lib/syslinux/bios")
    
    #for f in tools:
    #    pisitools.insinto(datadir, "utils/"+f) 

    pisitools.dodoc("README", "NEWS", "doc/*.txt", "doc/logo/LICENSE")
    pisitools.remove("/usr/bin/gethostip")
