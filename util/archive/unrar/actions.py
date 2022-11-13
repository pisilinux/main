#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcNAME()

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.copytree("unrar", "libunrar")
#changed for version 4.2.4
    autotools.make("-C libunrar lib")
    autotools.make("-C unrar -j1")
#autotools.make for older version
#    autotools.make('-f makefile.unix \
#                    CXXFLAGS="%s" \
#                    CXX="%s" \
#                    STRIP="true"' % (get.CXXFLAGS(), get.CXX()))

def install():
    autotools.rawInstall("DESTDIR=%s/usr" % get.installDIR())
    # pisitools.dobin("unrar")
    
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("libunrar")
    pisitools.doexe("libunrar.so", "/usr/lib")
    pisitools.insinto("/usr/include/unrar", "dll.hpp")
    
    pisitools.dodoc("readme.txt","license.txt")
