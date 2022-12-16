#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "-B build -DCMAKE_BUILD_TYPE=Release \
               -DWITH_JPEG8=TRUE \
               -DENABLE_STATIC=FALSE \
               -DCMAKE_INSTALL_DEFAULT_LIBDIR=lib \
               -DCMAKE_INSTALL_PREFIX=/usr"
               
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        
        options = "-B build -DCMAKE_INSTALL_DEFAULT_LIBDIR=/usr/lib32 \
                   -DCMAKE_INSTALL_PREFIX=/emul32"
    
    cmaketools.configure(options)

def build():
    cmaketools.make("-C build")
    
def check():
    shelltools.cd("build")
    cmaketools.make("test")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/*.pc" % get.installDIR(), "emul32", "usr")
        return
    
    # provide jpegint.h as it is required by various software
    #pisitools.insinto("/usr/lib/include", "jpegint.h")
    pisitools.insinto("/usr/include", "../jpegint.h")
