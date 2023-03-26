#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -e 's/^\(SUBDIRS =.*\)examples\(.*\)$/\1\2/' \
                                        -i Makefile.am Makefile.in || die")
    shelltools.system("sed -e 's/ -Werror/ /' -i tests/Makefile.am tests/Makefile.in || die")
    #autotools.autoreconf("-fi")
    autotools.configure()
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
