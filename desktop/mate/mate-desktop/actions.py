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
    #Change default xcursor
    #pisitools.dosed("schemas/org.mate.peripherals-mouse.gschema.xml.in", "<default>''</default>", "<default>'mate'</default>")
    pisitools.dosed("schemas/org.mate.background.gschema.xml.in", "backgrounds/mate/desktop/Stripes.png", "backgrounds/mate/nature/5.jpg")
    autotools.configure("--prefix=/usr \
                         --with-x \
                         --disable-static \
                         --disable-schemas-compile \
                         --disable-gtk-doc-html \
                         --enable-introspection=yes \
                         --enable-gtk-doc")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.dodoc("README", "NEWS")
