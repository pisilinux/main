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
    #pisitools.cflags.remove("-D_FORTIFY_SOURCE=2")
    #pisitools.cxxflags.remove("-D_FORTIFY_SOURCE=2")
    shelltools.export("AUTOPOINT", "true")
    options = "-Dpackage-name='PisiLinux gstreamer-plugins-base package' \
               -Dpackage-origin='https://www.pisilinux.org' \
               -Dgst-plugins-base:libvisual=disabled \
               -Dgst-plugins-base:tremor=disabled \
               -Dexamples=disabled \
              "
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        
        options += " --bindir=/usr/bin32 \
                     --libdir=/usr/lib32 \
                     -Dgl-graphene=disabled \
                     -Dintrospection=disabled \
                   "
                   
    else:
        options += "-Dgl-graphene=enabled"
    
    mesontools.configure(options)

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
