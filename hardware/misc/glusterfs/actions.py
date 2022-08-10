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
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.autoreconf("-fi")
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

    pisitools.dodir("/usr/lib/sysusers.d")
    shelltools.move("%s/usr/lib/tmpfiles.d/gluster.conf" % get.installDIR(), "%s/usr/lib/sysusers.d" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
