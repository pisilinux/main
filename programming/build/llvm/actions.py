# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

lib = "lib32" if get.buildTYPE() == "emul32" else "lib"
libdir = "/usr/%s/llvm" % lib


def setup():        
    options = "-DCMAKE_BUILD_TYPE=Release \
               -DLLVM_BUILD_LLVM_DYLIB=ON \
               -DLLVM_LINK_LLVM_DYLIB=ON \
               -DLLVM_INSTALL_UTILS=ON \
               -DLLVM_ENABLE_RTTI=ON \
               -DLLVM_ENABLE_FFI=ON \
               -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=AVR \
               -DLLVM_BUILD_TESTS=ON \
               -DLLVM_BUILD_DOCS=OFF \
               -DLLVM_ENABLE_SPHINX=ON \
               -DLLVM_ENABLE_DOXYGEN=OFF \
               -DSPHINX_WARNINGS_AS_ERRORS=OFF \
               -DFFI_INCLUDE_DIR=$(pkg-config --variable=includedir libffi) \
               -DLLVM_BINUTILS_INCDIR=/usr/include \
              " 
    if get.buildTYPE() != "emul32":
        if not shelltools.can_access_directory("tools/clang"):
                shelltools.move("../clang-%s.src" % get.srcVERSION(), "tools/clang")
                shelltools.move("../clang-tools-extra-%s.src" % get.srcVERSION(), "tools/clang/tools/extra")
                shelltools.move("../lld-%s.src" % get.srcVERSION(), "tools/lld")
                shelltools.move("../lldb-%s.src" % get.srcVERSION(), "tools/lldb")
                shelltools.move("../compiler-rt-%s.src" % get.srcVERSION(), "projects/compiler-rt")
                
    else:
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
    
    shelltools.makedirs("build")    
    shelltools.cd("build")
    
    if get.buildTYPE() != "emul32":
        options = "-DCMAKE_INSTALL_PREFIX=/usr \
                   -DLLVM_TARGET_ARCH:STRING=x86_64 \
                   -DLLVM_DEFAULT_TARGET_TRIPLE=%s  \
                   " % get.HOST()
    else:
        pisitools.flags.replace("-march=\S+", "-march=i686 -m32")
        options = "-DCMAKE_INSTALL_PREFIX=/emul32 \
                   -DLLVM_TARGET_ARCH:STRING=i686  \
                   -DLLVM_LIBDIR_SUFFIX=32 \
                   -DLLVM_DEFAULT_TARGET_TRIPLE='i686-pc-linux-gnu' \
                  "
    options += "-DCMAKE_C_FLAGS_RELEASE=%s \
                -DCMAKE_CXX_FLAGS_RELEASE=%s \
                " % (get.CFLAGS(), get.CXXFLAGS())    

    cmaketools.configure(options, sourceDir=".." ) 

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")    
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    if get.buildTYPE() == "emul32":
        
        pisitools.domove("/emul32/lib32/", "/usr/")
        pisitools.insinto("/usr/include/llvm/Config/","%s/emul32/include/llvm/Config/llvm-config.h" % get.installDIR(),"llvm-config-32.h")
        pisitools.insinto("/usr/bin/","%s/emul32/bin/llvm-config" % get.installDIR(),"llvm-config-32")
        pisitools.removeDir("/emul32")
        pisitools.remove("/usr/lib/python2.7/site-packages/six.py")
   
    shelltools.cd ("..")
    
    pisitools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
