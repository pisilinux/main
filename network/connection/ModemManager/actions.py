#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static \
                         --enable-more-warnings=yes \
                         --with-udev-base-dir=/lib/udev \
                         --enable-gtk-doc \
                         --enable-more-warnings=no \
                         --with-systemd-journal=no \
                         --with-systemd-suspend-resume=no \
                         --with-polkit=permissive")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
