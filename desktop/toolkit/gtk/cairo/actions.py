#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-flto -ffat-lto-objects")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-xlib \
                         --disable-drm \
                         --enable-xml=yes \
                         --enable-ft \
                         --enable-ps \
                         --enable-pdf \
                         --enable-svg \
                         --enable-tee=yes \
                         --enable-gl=yes \
                         --enable-gobject \
                         --enable-xcb \
                         --disable-gtk-doc")

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")
