# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    #shelltools.system("""sed -i 's:DESTINATION man/man1:DESTINATION "${CMAKE_INSTALL_PREFIX}/share/man/man1":g' \
    #doc/CMakeLists.txt""")
    # --shared and --release are default parameters, however we just write them
    # to down to avoid confusing wheter it's a static/shared or release/debug
    # package at the first look :)
    cmaketools.configure("-B build \
                          -DMAN_INSTALL_DIR=/usr/share/man/man1 \
                          -DCMAKE_INSTALL_PREFIX:PATH='/usr'")
    
def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.doman("../doc/doxygen.1")

    # The makefile included is there to generate the html files
    # The user itself should execute it
    pisitools.insinto(get.docDIR() + "/doxygen" , "../examples")

    shelltools.cd("..")
    pisitools.dodoc("LANGUAGE.HOWTO", "LICENSE", "README*", "VERSION")
