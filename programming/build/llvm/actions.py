# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"


def setup():
	
    if get.buildTYPE() != "emul32":
            if not shelltools.can_access_directory("tools/clang"):
                shelltools.system("tar xf ../cfe-%s.src.tar.xz -C tools" % get.srcVERSION())
                shelltools.move("tools/cfe-%s.src" % get.srcVERSION(), "tools/clang")

                shelltools.system("tar xf ../clang-tools-extra-%s.src.tar.xz -C tools" % get.srcVERSION())
                shelltools.move("tools/clang-tools-extra-*", "tools/clang/extra")
                
                shelltools.system("tar xf ../lldb-%s.src.tar.xz -C tools" % get.srcVERSION())
                shelltools.move("tools/lldb-*", "tools/lldb")
                
                shelltools.system("tar xf ../lld-%s.src.tar.xz -C tools" % get.srcVERSION())
                shelltools.move("tools/lld-*", "tools/lld")
                
                shelltools.system("tar xf ../polly-%s.src.tar.xz -C tools" % get.srcVERSION())
                shelltools.move("tools/polly-*", "tools/polly")

            if not shelltools.can_access_directory("projects/compiler-rt"):
                shelltools.system("tar xf ../compiler-rt-%s.src.tar.xz -C projects" % get.srcVERSION())
                shelltools.move("projects/compiler-rt-%s.src" % get.srcVERSION(), "projects/compiler-rt")
                

        
        
                shelltools.export("CC", "gcc")
                shelltools.export("CXX", "g++")
                
    
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
    
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    
    if get.buildTYPE() != "emul32":
        options = "-DCMAKE_C_FLAGS:STRING=-m64 \
                              -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_CXX_FLAGS:STRING=-m64 \
                            -DLLVM_TARGET_ARCH:STRING=x86_64 \
                            -DLLVM_DEFAULT_TARGET_TRIPLE=%s " % get.HOST()
                          
    
    if get.buildTYPE() == "emul32":
        options = "  -DCMAKE_C_FLAGS:STRING=-m32 \
                            -DCMAKE_INSTALL_PREFIX=/emul32 \
                            -DLLVM_TARGET_ARCH:STRING=i686  \
                            -DLLVM_LIBDIR_SUFFIX=32 \
                            -DLLVM_DEFAULT_TARGET_TRIPLE='i686-pc-linux-gnu' \
                            -DCMAKE_CXX_FLAGS:STRING=-m32"
    
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                                        %s \
                                        -DLLVM_ENABLE_FFI=ON \
                                        -DLLVM_BUILD_DOCS=OFF \
                                        -DLLVM_BUILD_LLVM_DYLIB=ON \
                                        -DLLVM_LINK_LLVM_DYLIB=ON \
                                        -DLLVM_ENABLE_RTTI=ON \
                                        -DLLVM_ENABLE_EH=ON \
                                        -DLLVM_INCLUDEDIR=/usr/include \
                                        -DLLVM_ENABLE_ASSERTIONS=OFF \
                                        -DFFI_INCLUDE_DIR=/usr/lib/libffi-3.2.1/include \
                                        -DENABLE_SHARED=ON" % options, sourceDir=".." ) 

def build():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.make()

def install():
    shelltools.makedirs("build")
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
