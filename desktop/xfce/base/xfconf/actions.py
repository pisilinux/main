#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

i = "--enable-introspection \
     --enable-vala=yes \
     --disable-static \
     --disable-gtk-doc \
     --disable-perl-bindings \
     --disable-gsettings-backend \
    "

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(i)

    #pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    #pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "TODO")

