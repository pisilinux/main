#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-ivf")
    shelltools.system("intltoolize --force --copy --automake")
    autotools.configure("--with-gtk=gtk3 \
                         --enable-icon-browser \
                         --enable-html \
                         --enable-gio \
                         --enable-spell \
                         --enable-sourceview")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
