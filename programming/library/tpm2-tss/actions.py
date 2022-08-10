#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("dist/tmpfiles.d/tpm2-tss-fapi.conf.in", "default:group:tss:rwx", deleteLine=True)

    shelltools.system("./bootstrap")
    autotools.configure("--enable-static=no \
                         --with-udevrulesprefix=60- \
                         --with-tmpfilesdir=/usr/lib/tmpfiles.d \
                         --with-sysusersdir=/usr/lib/sysusers.d")
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.move("%s/usr/lib/tmpfiles.d/tpm2-tss-fapi.conf" % get.installDIR(), "%s/usr/lib/sysusers.d" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
