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

WorkDir = "llvm-project-%s" %get.srcVERSION()

NoStrip = ["/usr"]

def setup():
	
    shelltools.export("CC", "clang")
    shelltools.export("CXX", "clang++")
    
    if get.buildTYPE() == "emul32" :
       libsuffix = "32"
       pisitools.ldflags.add(" -fuse-ld=lld -L/usr/lib32 -ldl -lpthread ")
       triple = "i686-pc-linux-gnu"       
       pisitools.cflags.add("-m32 --target=%s" %triple)
       pisitools.cxxflags.add("-m32 --target=%s" %triple)
    else:
       libsuffix = " "
       pisitools.ldflags.add(" -fuse-ld=lld -rtlib=compiler-rt -L/usr/lib -ldl -lpthread ")
       triple = "%s " % get.HOST()
       
    shelltools.system("ln -s %s/%s/libcxx llvm/projects/libcxx" %(get.workDIR(), WorkDir))
    shelltools.system("ln -s %s/%s/libcxxabi llvm/projects/libcxxabi" %(get.workDIR(), WorkDir))
    
    shelltools.makedirs("llvm/build")
    shelltools.cd("llvm/build")
    
    shelltools.system("   cmake \
		                  -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_AR=/usr/bin/llvm-ar \
                          -DCMAKE_RANLIB=/usr/bin/llvm-ranlib \
                          -DCMAKE_STRIP=' ' \
                          -DLIBCXXABI_USE_COMPILER_RT=ON \
                          -DLIBCXXABI_ENABLE_EXCEPTIONS=ON \
                          -DLIBCXXABI_ENABLE_THREADS=ON \
                          -DLIBCXXABI_ENABLE_SHARED=OFF \
                          -DLLVM_NO_OLD_LIBSTDCXX=TRUE \
                          -DCXX_SUPPORTS_CXX11=TRUE \
                          -DLIBCXXABI_ENABLE_SHARED=OFF \
                          -DLIBCXXABI_HAS_PTHREAD_API=ON \
                          -DLIBCXXABI_INSTALL_LIBRARY=OFF \
                          -DLIBCXXABI_INSTALL_STATIC_LIBRARY=OFF \
                          -DLIBCXXABI_ENABLE_NEW_DELETE_DEFINITIONS=OFF \
                          -DLIBCXXABI_ENABLE_STATIC_UNWINDER=ON \
                          -DLIBCXXABI_LIBUNWIND_INCLUDES=../../libunwind/incude  \
                          -DLIBCXXABI_LIBUNWIND_PATH=../../libunwind \
                          -DLIBCXXABI_USE_LLVM_UNWINDER=ON \
                          -DLIBCXX_INSTALL_HEADERS=ON \
                          -DLIBCXX_ENABLE_EXCEPTIONS=ON \
                          -DLIBCXX_ENABLE_THREADS=ON \
                          -DLIBCXX_ENABLE_MONOTONIC_CLOCK=ON \
                          -DLIBCXX_ENABLE_SHARED=ON \
                          -DLIBCXX_SUPPORTS_STD_EQ_CXX11_FLAG=TRUE \
                          -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=ON \
                          -DLIBCXX_ENABLE_FILESYSTEM=ON \
                          -DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=TRUE \
                          -DLIBCXX_USE_COMPILER_RT=ON \
                          -DLIBCXX_CXX_ABI=libcxxabi \
                          -DLIBCXX_HAS_PTHREAD_API=ON \
                          -DLIBCXX_LIBDIR_SUFFIX=%s \
                          -DLIBCXX_ENABLE_SHARED=ON \
                          -DLIBCXX_ENABLE_STATIC=ON \
                          -DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=TRUE \
                          -DLLVM_EXTERNAL_LIBUNWIND_SOURCE_DIR=../../libunwind \
                          -DLIBUNWIND_INSTALL_LIBRARY=OFF \
                          -DLIBUNWIND_ENABLE_SHARED=ON \
                          -DLIBUNWIND_USE_COMPILER_RT=ON \
                          -DLIBUNWIND_TARGET_TRIPLE=%s \
                          -DLLVM_DEFAULT_TARGET_TRIPLE=%s \
                          .. \
                        " %(libsuffix, triple, triple) )

def build():   
    shelltools.cd("llvm/build")
    autotools.make("cxx cxx_experimental")

def install():
    shelltools.cd("llvm/build")
    shelltools.system("DESTDIR=%s make install-cxx-headers install-cxx" %get.installDIR())
	
  
    pisitools.dodoc("../projects/libcxx/CREDITS.TXT", "../projects/libcxx/LICENSE.TXT", "../projects/libcxx/NOTES.TXT", "../projects/libcxx/TODO.TXT")
