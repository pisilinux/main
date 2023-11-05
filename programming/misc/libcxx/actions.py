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

WorkDir = "llvm-project-%s.src" % get.srcVERSION()

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
       options = "-DLLVM_ENABLE_RUNTIMES='libcxx;libcxxabi'"

    else:
       libsuffix = " "
       pisitools.ldflags.add(" -fuse-ld=lld -rtlib=compiler-rt -L/usr/lib -ldl -lpthread ")
       triple = "%s " % get.HOST()
       options = "-DLLVM_ENABLE_RUNTIMES='libcxx;libcxxabi;libunwind' -DLIBUNWIND_USE_COMPILER_RT=ON \
                             -DCMAKE_STRIP=' ' \
                             -DLIBCXXABI_USE_COMPILER_RT=ON \
                             -DLIBCXXABI_ENABLE_EXCEPTIONS=ON \
                             -DLIBCXXABI_ENABLE_THREADS=ON \
                             -DLIBCXXABI_ENABLE_SHARED=OFF \
                             -DLLVM_NO_OLD_LIBSTDCXX=TRUE \
                             -DLIBCXX_INSTALL_HEADERS=ON \
                             -DLIBCXX_ENABLE_EXCEPTIONS=ON \
                             -DLIBCXX_ENABLE_THREADS=ON \
                             -DLIBCXX_ENABLE_MONOTONIC_CLOCK=ON \
                             -DLIBCXX_ENABLE_SHARED=ON \
                             -DLIBCXX_SUPPORTS_STD_EQ_CXX11_FLAG=TRUE \
                             -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=ON \
                             -DLIBCXX_ENABLE_FILESYSTEM=ON \
                             -DLIBCXX_USE_COMPILER_RT=ON \
                             -DLIBCXX_HAS_PTHREAD_API=ON \
                             -DLIBUNWIND_ENABLE_SHARED=ON \
                             -DLIBCXXABI_ENABLE_STATIC_UNWINDER=ON \
                             -DLIBCXXABI_USE_LLVM_UNWINDER=ON \
                             -DLIBCXX_ENABLE_SHARED=ON \
                             -DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=TRUE \
                             -DCXX_SUPPORTS_CXX11=TRUE \
                             -DLIBCXX_ENABLE_STATIC=ON \
                             -DLIBUNWIND_TARGET_TRIPLE=%s \
                            " % triple
       
    # shelltools.system("ln -s %s/%s/libcxx llvm/projects/libcxx" %(get.workDIR(), WorkDir))
    # shelltools.system("ln -s %s/%s/libcxxabi llvm/projects/libcxxabi" %(get.workDIR(), WorkDir))
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    shelltools.system("   cmake \
		                  -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIBCXX_LIBDIR_SUFFIX=%s \
                          -DCMAKE_C_COMPILER=clang \
                          -DCMAKE_CXX_COMPILER=clang++ \
                          -DLLVM_ENABLE_PIC=ON \
                          -DLLVM_DEFAULT_TARGET_TRIPLE=%s \
                          %s \
                          ../runtimes \
                        " %(libsuffix, triple, options) )

def build():   
    shelltools.cd("build")
    autotools.make("cxx cxx_experimental")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s make install-cxx-headers install-cxx" %get.installDIR())
	
  
    pisitools.dodoc("../libcxx/CREDITS.TXT", "../libcxx/LICENSE.TXT", "../libcxx/TODO.TXT")
