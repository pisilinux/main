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
    autotools.autoreconf("-fi")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-static \
                         --sbindir=/usr/bin \
                         --with-mountutildir=/usr/bin \
                         --prefix=/usr \
                         --without-selinux \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --mandir=/usr/share/man \
                         --libexecdir=/usr/lib \
                         --with-tmpfilesdir=/usr/lib/tmpfiles.d \
                         --enable-gnfs")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
