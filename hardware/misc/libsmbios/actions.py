#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("./autogen.sh --no-configure")
    #autotools.autoreconf("-fi")
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure --prefix=/usr --sbindir=/usr/sbin --sysconfdir=/etc --disable-static --enable-libsmbios_cxx")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include", "../src/include/*")
    pisitools.insinto("/usr/include", "out/public-include/*")

    # Symlink to /usr/sbin/DellWirelessCtl for the new HAL
    pisitools.dosym("/usr/sbin/smbios-wireless-ctl", "/usr/sbin/DellWirelessCtl")

    # Remove yum specific stuff
    #pisitools.removeDir("/etc/yum")
    #pisitools.removeDir("/usr/bin")
    #pisitools.removeDir("/usr/lib/yum-plugins")
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "README*")
