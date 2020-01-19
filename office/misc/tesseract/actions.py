#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static")
    # fıx unused dırect dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()
    autotools.make("training")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make("training-install DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("LICENSE", "README*")