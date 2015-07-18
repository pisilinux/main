#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
     #pisitools.ldflags.add("-Wl,-rpath")
    
    #shelltools.system("sed -i -e 's|add_subdirectory(dolphin)|#add_subdirectory(dolphin)|' CMakeLists.txt")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DKDE4_BUILD_TESTS=OFF \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README", "COPYING.LIB")
