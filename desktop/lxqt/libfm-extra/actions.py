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
    autotools.configure("--sysconfdir=/etc \
                         --with-extra-only \
                         --with-gtk=no     \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/include/libfm")
    pisitools.dodir("/usr/include/libfm")
    pisitools.domove("/usr/include/libfm-1.0/*", "/usr/include/libfm")
    pisitools.removeDir("/usr/include/libfm-1.0")
    pisitools.dodoc("AUTHORS", "COPYING")
