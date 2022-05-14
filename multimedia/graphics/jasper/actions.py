#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -r 's|(CMAKE_SKIP_BUILD_RPATH) FALSE|\1 TRUE|g' -i CMakeLists.txt")
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    if get.buildTYPE() != "emul32":
        options = "-DCMAKE_INSTALL_PREFIX=/usr \
                   -DCMAKE_INSTALL_LIBDIR=lib"
    
    if get.buildTYPE() == "emul32":
        options = "-DCMAKE_INSTALL_PREFIX=/emul32 \
                   -DCMAKE_INSTALL_LIBDIR=lib32"
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                                        %s \
                          -DALLOW_IN_SOURCE_BUILD=ON     \
                          -DCMAKE_JAS_ENABLE_AUTOMATIC_DEPENDENCIES=false \
                          -DCMAKE_SKIP_INSTALL_RPATH=YES" % options, sourceDir=".." )

def build():
    shelltools.cd("build")
    
    cmaketools.make()

def install():
    shelltools.cd("build")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.domove("/emul32/lib32/", "/usr/")
        pisitools.removeDir("/emul32")

    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README")
