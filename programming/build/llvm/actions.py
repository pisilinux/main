# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

projects = "clang;mlir" if get.buildTYPE() == "emul32" else "clang;clang-tools-extra;lld;lldb;polly;compiler-rt;mlir"
libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"
libsuffix = "32" if get.buildTYPE() == "emul32" else " "

NoStrip = ["/usr/lib/clang/%s/lib/linux" %get.srcVERSION()]

WorkDir = "llvm-project-%s" % get.srcVERSION()

def setup():
    #pisitools.ldflags.add("-fuse-ld=lld -rtlib=libgcc")
    #pisitools.cflags.remove("-D_FORTIFY_SOURCE=2")
    #pisitools.cxxflags.remove("-D_FORTIFY_SOURCE=2")
    

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        #shelltools.export("CC", "clang -m32")
        #shelltools.export("CXX", "clang++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        
        #clang patch
        #shelltools.cd("tools")
        #shelltools.system("patch -p1 < enable-SSP-and-PIE-by-default.patch")
        #shelltools.cd("..")
    else:
        shelltools.export("CC", "gcc")
        shelltools.export("CXX", "g++")
        #shelltools.export("CC", "clang")
        #shelltools.export("CXX", "clang++")
    
    shelltools.makedirs("llvm/build")
    
    shelltools.cd("llvm/build")
    
    if get.buildTYPE() != "emul32":
        pisitools.cflags.add("-m64")
        pisitools.cxxflags.add("-m64")
        options = "-DLLVM_TARGET_ARCH:STRING=x86_64 \
                   -DLLDB_ENABLE_LUA=OFF \
                   -DLLVM_DEFAULT_TARGET_TRIPLE=%s " % get.HOST()
                          
    
    if get.buildTYPE() == "emul32":
        pisitools.cflags.add("-m32")
        pisitools.cxxflags.add("-m32")
        options = "  -DCMAKE_INSTALL_PREFIX=/emul32 \
                     -DLLVM_TARGET_ARCH:STRING=i686  \
                     -DLLVM_DEFAULT_TARGET_TRIPLE='i686-pc-linux-gnu'"
    
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -G 'Ninja' \
                          %s \
                          -DLLVM_ENABLE_PROJECTS='%s' \
                          -DLLVM_LIBDIR_SUFFIX=%s \
                          -DLLVM_ENABLE_FFI=ON \
                          -DLLVM_BUILD_DOCS=OFF \
                          -DLLVM_ENABLE_RTTI=ON \
                          -DLLVM_ENABLE_EH=ON \
                          -DLLVM_BUILD_LLVM_DYLIB=ON \
                          -DLLVM_LINK_LLVM_DYLIB=ON \
                          -DCLANG_LINK_CLANG_DYLIB=ON \
                          -DLLDB_USE_SYSTEM_SIX=1 \
                          -DLLVM_INCLUDEDIR=/usr/include \
                          -DLLVM_ENABLE_ASSERTIONS=OFF \
                          -DFFI_INCLUDE_DIR=/usr/include \
                          -DCOMPILER_RT_USE_LIBCXX=OFF" % (options, projects, libsuffix), sourceDir=".." ) 

def build():
    shelltools.cd("llvm/build")
    shelltools.system("ninja")
    #cmaketools.make()

def install():
    shelltools.cd("llvm/build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    if get.buildTYPE() == "emul32":        
        pisitools.domove("/emul32/lib32/", "/usr/")
        pisitools.insinto("/usr/include/llvm/Config/","%s/emul32/include/llvm/Config/llvm-config.h" % get.installDIR(),"llvm-config-32.h")
        pisitools.insinto("/usr/bin/","%s/emul32/bin/llvm-config" % get.installDIR(),"llvm-config-32")
        pisitools.removeDir("/emul32")
        #pisitools.remove("/usr/lib/python3.8/site-packages/six.py")
   
    shelltools.cd ("..")
    
    pisitools.dodoc("LICENSE.TXT", "README.txt")
