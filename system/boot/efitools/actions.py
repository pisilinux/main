#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system('sed -i "s/-O2/${CFLAGS} -Wno-pointer-sign/" Make.rules')
    shelltools.export("ARCH","x86_64")
    
    autotools.make()

def install():
    shelltools.export("ARCH","x86_64")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("COPYING", "README")
