#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    #shelltools.makedirs("build")
    #shelltools.cd("build")

    options = "-DCMAKE_BUILD_TYPE=Release \
               -DCMAKE_INSTALL_LIBDIR=/usr/lib \
               -DCMAKE_INSTALL_PREFIX=/usr \
               -DBUILD_SHARED_LIBS=ON \
               -DBUILD_STATIC_LIBS=OFF \
               -DBUILD_DOC=on"
               
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        
        options = "-DOPENJPEG_INSTALL_LIB_DIR=lib32 \
                   -DCMAKE_INSTALL_PREFIX=/usr \
                   -DOPENJPEG_INSTALL_BIN_DIR=emul32 \
                   -DBUILD_DOC=OFF"
    
    cmaketools.configure(options)

def build():
    #shelltools.cd("build")
    cmaketools.make()

def install():
    #shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/bin/","%s/usr/emul32/opj_compress" % get.installDIR(),"opj_compress_32")
        pisitools.insinto("/usr/bin/","%s/usr/emul32/opj_decompress" % get.installDIR(),"opj_decompress_32")
        pisitools.insinto("/usr/bin/","%s/usr/emul32/opj_dump" % get.installDIR(),"opj_dump_32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/libopenjp2.pc" % get.installDIR(), "emul32", "bin")
        pisitools.dosed("%s/usr/lib32/openjpeg-2.3/OpenJPEGTargets-relwithdebinfo.cmake" % get.installDIR(), "emul32", "bin")
        pisitools.removeDir("/usr/emul32")
        
        
        pisitools.dodoc("AUTHORS*", "CHANGELOG*", "NEWS*", "README*")
        
