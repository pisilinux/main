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
    autotools.autoreconf("-ivf")
    shelltools.system("intltoolize --force --copy --automake")
    autotools.configure("--enable-gio \
                         --enable-html \
                         --enable-spell \
                         --with-gtk=gtk3 \
                         --enable-sourceview \
                         --enable-icon-browser")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")