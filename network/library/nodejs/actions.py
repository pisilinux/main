#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j2"))

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --shared-libuv \
                            --shared-openssl \
                            --shared-nghttp2 \
                            --shared-zlib \
                            ")
                            # --with-intl=system-icu
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
