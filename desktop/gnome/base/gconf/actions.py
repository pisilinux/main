#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    #autotools.autoreconf("-fiv")
    shelltools.system("sed -i '1s|#!/usr/bin/env python$|&2|' gsettings/gsettings-schema-convert")
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib/GConf \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-orbit \
                         --enable-defaults-service \
                         --with-pic \
                         --with-gtk=3.0 \
                        ")
    #pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    #pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("pkglibdir=/usr/lib/GConf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
