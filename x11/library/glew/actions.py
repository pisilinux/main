#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -i 's|lib64|lib|' config/Makefile.linux")
    shelltools.system("sed -i '/^.PHONY: .*\.pc$/d' Makefile")
    
    if get.buildTYPE() == "emul32":
        pisitools.dosed("config/Makefile.linux", "LD = cc", "LD = gcc -m32")
        shelltools.system("sed -i 's|lib64|lib32|' config/Makefile.linux")
        autotools.make('CC="%s -m32" CXXFLAGS="%s" LIBDIR=/usr/lib32' % (get.CC(), get.CXXFLAGS()))
        return
    else:
        autotools.make('CC=%s CXXFLAGS="%s"' % (get.CC(), get.CXXFLAGS()))
        return

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("GLEW_DEST=%s/usr/ \
                              INCDIR=%s/emul32 \
                              BINDIR=%s/emul32 \
                              LIBDIR=%s/usr/lib32 \
                              PKGDIR=%s/usr/lib32/pkgconfig" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))

        pisitools.remove("/usr/lib32/libGLEW.a")
        #pisitools.dosed("%s/usr/lib32/pkgconfig/glew.pc" % get.installDIR(), "/usr/lib", "/usr/lib32")
        return

    autotools.rawInstall("GLEW_DEST=%s/usr/ \
                          INCDIR=%s/usr/include/GL \
                          BINDIR=%s/usr/bin \
                          LIBDIR=%s/usr/lib" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.dobin("bin/glewinfo")
    pisitools.dobin("bin/visualinfo")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("README.md", "doc/*.txt", "LICENSE.txt")
