#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    options = "-Dpackage-name='GStreamer for PisiLinux' \
               -Dpackage-origin='https://www.pisilinux.org' \
               -Dptp-helper-permissions=capabilities \
               -Ddbghelp=disabled \
              "
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        
        options += " --bindir=/usr/bin32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/usr/libexec32 \
                     -Dintrospection=disabled \
                   "
    
    mesontools.configure(options)

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        pisitools.removeDir("/usr/libexec32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README*")
