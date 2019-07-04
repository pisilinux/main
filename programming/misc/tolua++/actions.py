#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    
    cmaketools.configure("-DLUA_EXECUTABLE=/usr/lib/lua5.1 \
		                  -DLUA_INCLUDE_DIR=/usr/include/lua5.1 \
		                  -DLUA_LIBRARY=/usr/lib/liblua5.1.so \
		                  ")
    cmaketools.make()

    # Remove static libraries
    #shelltools.unlink(get.workDIR()+'/'+get.srcDIR()+'/lib/*.a')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("COPYRIGHT", "README*")
