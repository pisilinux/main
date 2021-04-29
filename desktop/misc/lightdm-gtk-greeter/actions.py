#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(" --prefix=/usr \
                                    --libexecdir=/usr/lib/lightdm \
                                    --sbindir=/usr/bin \
                                    --sysconfdir=/etc \
                                    --with-libxklavier \
                                    --enable-kill-on-sigterm \
                                    --disable-libido \
                                    --disable-libindicator \
                                    --disable-static \
                                    --with-gtk3 \
                                    --enable-nls")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
