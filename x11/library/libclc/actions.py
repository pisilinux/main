#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib" 

def setup():
    pisitools.dosed("CMakeLists.txt", "{CMAKE_INSTALL_DATADIR}", "{CMAKE_INSTALL_LIBDIR}")
	
    if get.buildTYPE() == "emul32": 
       shelltools.system("chmod +x clang32")
       options = "-DLLVM_CLANG='%s/%s-%s.src/clang32' \
                  -DLLVM_CONFIG='/usr/bin/llvm-config-32' \
                  -DCMAKE_INSTALL_LIBDIR=lib32 \
                 " % (get.workDIR(), get.srcNAME(), get.srcVERSION())
    else:
       options = "-DLLVM_CLANG='/usr/bin/clang' \
                  -DLLVM_CONFIG='/usr/bin/llvm-config' \
                  -DCMAKE_INSTALL_LIBDIR=lib \
                 "
	
    cmaketools.configure(options)
    
def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.domove("/usr/share/clc/", "%s" %libdir)
    #pisitools.domove("/usr/share/pkgconfig/libclc.pc", "%s/pkgconfig" % libdir)
    
    if get.buildTYPE() == "emul32":
       shelltools.system("sed -i 's/\/usr\/share/\/usr\/lib32/' %s/usr/lib32/pkgconfig/libclc.pc" % get.installDIR())
    else:
       shelltools.system("sed -i 's/\/usr\/share/\/usr\/lib/' %s/usr/lib/pkgconfig/libclc.pc" % get.installDIR())
       
    #pisitools.removeDir("/usr/share/clc")
    #pisitools.removeDir("/usr/share/pkgconfig")
    
    pisitools.dodoc("LICENSE*", "README*")
