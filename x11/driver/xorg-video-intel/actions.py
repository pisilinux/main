# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # DRI3 has been known to be buggy with the current stack, so is disabled

    
    #shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.autoreconf("-fi")
    pisitools.cflags.add("-fno-plt")
    pisitools.cxxflags.add("-fno-plt")
    pisitools.ldflags.add("-z,now")

    autotools.configure("--enable-dri \
                         --enable-sna \
                         --enable-uxa")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

  #  pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
