# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
	
	pisitools.cflags.add("-fno-plt -fcommon")
	pisitools.cxxflags.add("-fno-plt")
	pisitools.ldflags.add(",-z,now")
	
    autotools.autoreconf("-fiv")
    autotools.configure("\
                         --disable-static \
                         --enable-glamor \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "ChangeLog", "README")
