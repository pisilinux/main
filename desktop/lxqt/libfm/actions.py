#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-udisks \
                         --disable-static \
                         --with-gtk=3 \
                         --with-gnu-ld")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())    
    pisitools.remove("/usr/include/libfm")
    pisitools.dodir("/usr/include/libfm")
    pisitools.domove("/usr/include/libfm-1.0/*.*", "/usr/include/libfm")    
    pisitools.removeDir("/usr/include/libfm-1.0") 
    pisitools.remove("/usr/include/libfm/fm-version.h")
    pisitools.remove("/usr/include/libfm/fm-extra.h")
    pisitools.remove("/usr/include/libfm/fm-xml-file.h")
    pisitools.remove("/usr/lib/libfm-extra*")
    pisitools.remove("/usr/lib/pkgconfig/libfm-extra.pc")
    pisitools.dodoc("AUTHORS", "COPYING")
