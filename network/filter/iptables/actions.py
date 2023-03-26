#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("rm -f include/linux/{kernel,types}.h")
    autotools.autoreconf("-fiv")
    autotools.configure("--sbindir=/sbin \
                         --libexecdir=/usr/lib \
                         --enable-bpf-compiler \
                         --enable-devel \
                         --enable-libipq \
                         --enable-shared \
                         --enable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/usr/include", "include/iptables.h")
    pisitools.insinto("/usr/include", "include/ip6tables.h")
    pisitools.insinto("/usr/include/libiptc", "include/libiptc/*.h")

    pisitools.dodir("/var/lib/iptables")
    pisitools.dodir("/var/lock/subsys")
    pisitools.dodir("/etc/iptables")
