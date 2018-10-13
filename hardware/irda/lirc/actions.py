#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "-")

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--localstatedir=/run \
                         --with-systemdsystemunitdir=no \
                         --enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --with-x")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("contrib/irman2lirc")

    # needed for lircd pid
    pisitools.dodir("/run/lirc")

    # example configs
    pisitools.insinto("/etc", "contrib/lircd.conf", "lircd.conf")
    pisitools.insinto("/etc", "contrib/lircmd.conf", "lircmd.conf")

    pisitools.dohtml("doc/html/*.html")
    pisitools.rename("/%s/%s" % (get.docDIR(), get.srcNAME()), "lirc")

    pisitools.insinto("/%s/lirc/contrib" % get.docDIR(), "contrib/*")
    pisitools.insinto("/lib/udev/rules.d", "contrib/*.rules", "60-lirc.rules")
    
    pisitools.domove("/run/lib/lirc/*", "/var/lib/lirc")
    pisitools.removeDir("/run/lib")

