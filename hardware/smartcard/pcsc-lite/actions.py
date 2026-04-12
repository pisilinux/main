#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr -Dserial=true -Dlibsystemd=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodir("/etc/reader.conf.d")
    pisitools.dodir("/usr/lib/pcsc/drivers")

    #for fixing UYAP e-Sign problem
    pisitools.dodir("/usr/lib/x86_64-linux-gnu/")
    libs=["libpcsclite.so", "libpcsclite.so.1"]
    for l in libs:
        pisitools.dosym("/usr/lib/%s" % l, "/usr/lib/x86_64-linux-gnu/%s" % l)

    pisitools.dodoc("AUTHORS", "COPYING")
