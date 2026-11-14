#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools



WorkDir = "llvm-project-%s.src/runtimes" % get.srcVERSION()

libdir = "/usr/lib32" if get.buildTYPE() == 'emul32' else "/usr/lib"

def setup():
    
    #shelltools.export("CC", "clang")
    #shelltools.export("CXX", "clang++")
    #pisitools.ldflags.add("-fuse-ld=lld -rtlib=compiler-rt -stdlib=libc++")
    
    options = "cmake -B build -DCMAKE_BUILD_TYPE=Release \
               -DLIBOMP_ENABLE_ASSERTIONS=ON \
               -DLIBOMP_ENABLE_SHARED=ON \
               -DLIBOMP_USE_HIER_SCHED=ON \
               -DLLVM_ENABLE_RUNTIMES=openmp \
               -DCMAKE_INSTALL_LIBDIR=%s \
               -DOPENMP_INSTALL_LIBDIR=%s \
              " % (libdir, libdir)
              # -DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON \
              # -DLIBOMP_OMPD_SUPPORT=OFF \
               # -DLIBOMP_OMPT_SUPPORT=OFF \
               
    if get.buildTYPE() == "emul32":
         pisitools.cflags.add("-m32")
         pisitools.cxxflags.add("-m32")                   
         options += " -DOPENMP_LIBDIR_SUFFIX=32 \
                   "
    else:
         pisitools.cflags.add("-m64")
         pisitools.cxxflags.add("-m64")
         options += "-DOPENMP_LIBDIR_SUFFIX=  \
                   "

    cmaketools.configure(options)
    

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
	
    if get.buildTYPE() == "emul32":
       pisitools.remove("/usr/lib32/libgomp.so")
       pisitools.remove("/usr/lib32/libarcher_static.a")
    else:
       pisitools.remove("/usr/lib/libgomp.so")
       pisitools.remove("/usr/lib/libarcher_static.a")


    #pisitools.removeDir("/usr/share/gtk-doc")
    shelltools.cd("../..")
    pisitools.dodoc("LICENSE.*", "README.*")
