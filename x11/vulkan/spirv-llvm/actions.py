#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

tools = "-DLLVM_BUILD_TOOLS=OFF" if get.buildTYPE() == "emul32" else "-DLLVM_BUILD_TOOLS=ON"
libdir = "lib32" if get.buildTYPE() == "emul32" else "lib"

def setup():
    options = "-DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DLLVM_SPIRV_BUILD_EXTERNAL=YES \
                          -DLLVM_INCLUDE_TESTS=ON \
                          -DLLVM_EXTERNAL_LIT=/usr/bin/lit \
                          -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=/usr/include/spirv/ \
                          -DCMAKE_INSTALL_LIBDIR=%s \
                          %s \
                          -Wno-dev" % (libdir, tools)

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

        options += " -DLLVM_LIBDIR_SUFFIX=32 \
                             -DCMAKE_INSTALL_BINDIR:PATH=bin32 \

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodoc("LICENSE*", "README*")
