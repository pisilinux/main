#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()
    #shelltools.export("CFLAGS", "%s -O2 -DIP_MAX_MEMBERSHIPS=20" % get.CFLAGS())

    #autotools.autoreconf("-vfi")
    #autotools.configure("--enable-ipv6 \
    #                     --with-ssl \
    #                     --with-smi \
    #                     --enable-ipv6 \
    #                     --disable-smb \
    #                     --mandir=/usr/share/man")

def build():
    autotools.make()
    
def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/bin/tcpdump.%s" % get.srcVERSION())
    #pisitools.dosbin("tcpdump")
    #pisitools.doman("tcpdump.1")
    #pisitools.dodoc("CHANGES", "LICENSE", "README", "CREDITS", "PLATFORMS", "VERSION", "*.awk")
