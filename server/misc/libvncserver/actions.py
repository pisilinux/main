#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "libvncserver-LibVNCServer-%s" % get.srcVERSION()

def setup():
    #autotools.autoreconf("-vif")
    #autotools.configure("--disable-static \
                         #--disable-dependency-tracking \
                         #--with-24bpp \
                         #--with-zlib \
                         #--with-jpeg")

    #pisitools.dosed("libtool", " -shared ", " -shared -Wl,--as-needed")
    
    cmaketools.configure("-DWITH_FFMPEG=OFF \
                          -DWITH_SASL=OFF \
                          -DWITH_SDL=OFF \
                          -DWITH_SYSTEMD=OFF \
                          ")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.remove("/usr/bin/linuxvnc")
