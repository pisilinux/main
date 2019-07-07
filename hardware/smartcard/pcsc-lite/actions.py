#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

USBDROPDIR = "/usr/lib/pcsc/drivers"

def setup():
    options = "--enable-usbdropdir=%s \
               --disable-libsystemd \
               --disable-dependency-tracking \
               --disable-static" % USBDROPDIR


    autotools.autoreconf("-fi")
    autotools.configure(options)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir(USBDROPDIR)

    pisitools.dodir("/etc/reader.conf.d")

    #for fixing UYAP e-Sign problem
    pisitools.dodir("/usr/lib/x86_64-linux-gnu/")
    libs=["libpcsclite.so","libpcsclite.so.1", "libpcsclite.so.1.0.0"]
    for i in libs:
        pisitools.dosym("/usr/lib/%s" % i, "/usr/lib/x86_64-linux-gnu/%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "HELP", "NEWS",
                    "README", "SECURITY", "doc/README.DAEMON")
