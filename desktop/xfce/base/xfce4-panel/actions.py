#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "--enable-introspection  \
     --enable-gtk-doc  \
     --enable-gio-unix  \
     --enable-vala=yes \
     --disable-debug  \
     --disable-static \
    "

def setup():
    pisitools.cflags.add("-Wno-deprecated-declarations")
    autotools.configure(i)

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS*")
