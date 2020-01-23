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


def setup():
    
    shelltools.export("CC", "clang -fuse-ld=lld -rtlib=compiler-rt")
    shelltools.export("CXX", "clang++ -fuse-ld=lld -rtlib=compiler-rt -stdlib=libc++")
    
    options = "-DCMAKE_BUILD_TYPE=Release \
               -DLIBOMP_ENABLE_ASSERTIONS=ON \
               -DLIBOMP_ENABLE_SHARED=ON \
               -DLIBOMP_USE_HIER_SCHED=ON \
              "
               
    if get.buildTYPE() == "emul32":        
                     
         options = " -DOPENMP_LIBDIR_SUFFIX=32 \
                   "
    else:
           options = "-DOPENMP_LIBDIR_SUFFIX= \
                     "

    cmaketools.configure(options)
    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
	
    if get.buildTYPE() == "emul32":
       pisitools.remove("/usr/lib32/libgomp.so")
    else:
       pisitools.remove("/usr/lib/libgomp.so")


    #pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("CREDITS.txt", "LICENSE.txt", "README.rst")
