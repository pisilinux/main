#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "llvm-project-%s/flang"

NoStrip = ["/usr"]

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    if get.buildTYPE() == "emul32":
       shelltools.export("CC", "clang")
       shelltools.export("CXX" "clang++")
    else:
       shelltools.export("CC", "clang -m32")
       shelltools.export("CXX" "clang++ -m32")

    pisitools.ldflags.add("-fuse-ld=lld")
    
    options = "-DBUILD_SHARED_LIBS=ON \
               -DFLANG_INCLUDE_DOCS=ON \
               -DLLVM_LINK_LLVM_DYLIB=ON \
               -DLLVM_EXTERNAL_LIT=../../llvm/utils/lit/lit.py \
              "
    if get.buildTYPE() == "emul32":
       options += "-DLLVM_LIBDIR_SUFFIX=32 \
                   -DCMAKE_INSTALL_PREFIX=/emul32
                  "
    cmaketools.configure(options)

def build():   
    shelltools.cd("build")
    autotools.make()
    
def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    if get.buildTYPE() == "emul32" :
       pisitools.domove("/emul32/lib32/", "/usr/")
       pisitools.removeDir("/emul32")
   
    pisitools.dodoc("LICENSE.TXT", "README.md")
