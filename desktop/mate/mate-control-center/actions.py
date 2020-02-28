#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    #shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-static \
                         --libexecdir=/usr/bin/mate-control-center \
                         --sbindir=/usr/bin \
                         --with-gnu-ld \
                         --disable-update-mimedb \
                         --disable-schemas-compile")

    # fix unused-direct-shlib-dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,-O1--as-needed -shared ")



def build():
    autotools.make()

def install():
    #pisitools.dodir("/usr/lib")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS", "TODO")

    pisitools.remove("/usr/share/applications/mimeinfo.cache")
