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
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib/mate-utils \
                         --disable-static \
                         --disable-schemas-compile \
                         --enable-gdict-applet \
                         --enable-gtk-doc-html \
                         --enable-ipv6=yes \
                         --disable-maintainer-flags \
                         --disable-schemas-compile \
                         --with-x")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
