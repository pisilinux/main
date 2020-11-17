# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

projects = "clang;polly;compiler-rt;mlir" if get.buildTYPE() == "emul32" else "clang;clang-tools-extra;lld;lldb;polly;compiler-rt;mlir"
libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"
libsuffix = "32" if get.buildTYPE() == "emul32" else ""

NoStrip = ["/usr/lib/clang/%s/lib/linux" %get.srcVERSION()]

WorkDir = "llvm-project-%s/llvm" %get.srcVERSION()

def setup():
    pisitools.ldflags.add("-fuse-ld=lld")
    pisitools.cflags.remove("-D_FORTIFY_SOURCE=2")
    pisitools.cxxflags.remove("-D_FORTIFY_SOURCE=2")
    

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "clang -m32")
        shelltools.export("CXX", "clang++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        
        #clang patch
        #shelltools.cd("tools")
        #shelltools.system("patch -p1 < enable-SSP-and-PIE-by-default.patch")
        #shelltools.cd("..")
    else:
        shelltools.export("CC", "clang")
        shelltools.export("CXX", "clang++")
    
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    
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
                     -DLLVM_LIBDIR_SUFFIX=32 \
                     -DLLVM_DEFAULT_TARGET_TRIPLE='i686-pc-linux-gnu'"
    
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -G 'Unix Makefiles' \
                          %s \
                          -DLLVM_ENABLE_PROJECTS='%s' \
                          -DLLVM_ENABLE_FFI=ON \
                          -DLLVM_BUILD_DOCS=OFF \
                          -DLLVM_ENABLE_RTTI=ON \
                          -DLLVM_ENABLE_EH=ON \
                          -DBUILD_SHARED_LIBS=ON \
                          -DLLVM_INCLUDEDIR=/usr/include \
                          -DLLVM_ENABLE_ASSERTIONS=OFF \
                          -DFFI_INCLUDE_DIR=/usr/include \
                          -DCOMPILER_RT_USE_LIBCXX=OFF \
                          -DCLANG_DEFAULT_RTLIB=compiler-rt \
                          .. " % (options, projects), sourceDir=".." ) 

def build():
    shelltools.makedirs("build")
    shelltools.cd("build")

    autotools.make()

def install():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    if get.buildTYPE() == "emul32":        
        pisitools.domove("/emul32/lib32/", "/usr/")
        pisitools.insinto("/usr/include/llvm/Config/","%s/emul32/include/llvm/Config/llvm-config.h" % get.installDIR(),"llvm-config-32.h")
        pisitools.insinto("/usr/bin/","%s/emul32/bin/llvm-config" % get.installDIR(),"llvm-config-32")
        pisitools.removeDir("/emul32")
        #pisitools.remove("/usr/lib/python2.7/site-packages/six.py")
   
    shelltools.cd ("..")
       
    pisitools.dodoc("LICENSE.TXT", "README.txt")
