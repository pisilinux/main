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
    pisitools.dosed("configure", "-Werror=format", "#-Werror=format")
    shelltools.export("PYTHON", "/usr/bin/python3.6")
    shelltools.system("./configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/lib/pkgconfig/pygobject-3.0.pc", "py3gobject-3.0.pc")
    pisitools.rename("/usr/include/pygobject-3.0/pygobject.h", "py3gobject.h") 
    
    pisitools.dodoc("ChangeLog", "README*")

    
