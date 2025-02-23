#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="icu/source"

def setup():
    autotools.autoconf("-f")
    options = "--with-data-packaging=library \
               --disable-samples \
               --disable-silent-rules"
               
    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin"
        
    autotools.configure(options)
    pisitools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

def build():
    autotools.make()

def check():
    autotools.make("-k check || true")

def install():
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())
    if get.buildTYPE() == "_emul32":
        pisitools.domove("/_emul32/bin/icu-config", "/usr/bin", "icu-config-32")
        pisitools.removeDir("/_emul32")

        # pisitools.dosym("/usr/lib/libicudata.so.76.1", "/usr/lib/libicudata.so.73")
        # pisitools.dosym("/usr/lib/libicui18n.so.76.1", "/usr/lib/libicui18n.so.73")
        # pisitools.dosym("/usr/lib/libicuio.so.76.1", "/usr/lib/libicuio.so.73")
        # pisitools.dosym("/usr/lib/libicutest.so.76.1", "/usr/lib/libicutest.so.73")
        # pisitools.dosym("/usr/lib/libicutu.so.76.1", "/usr/lib/libicutu.so.73")
        # pisitools.dosym("/usr/lib/libicuuc.so.76.1", "/usr/lib/libicuuc.so.73")

        # pisitools.dosym("/usr/lib32/libicudata.so.76.1", "/usr/lib32/libicudata.so.73")
        # pisitools.dosym("/usr/lib32/libicui18n.so.76.1", "/usr/lib32/libicui18n.so.73")
        # pisitools.dosym("/usr/lib32/libicuio.so.76.1", "/usr/lib32/libicuio.so.73")
        # pisitools.dosym("/usr/lib32/libicutest.so.76.1", "/usr/lib32/libicutest.so.73")
        # pisitools.dosym("/usr/lib32/libicutu.so.76.1", "/usr/lib32/libicutu.so.73")
        # pisitools.dosym("/usr/lib32/libicuuc.so.76.1", "/usr/lib32/libicuuc.so.73")

        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "_emul32", "usr") 
            pisitools.dosed("%s/usr/lib32/icu/%s/Makefile.inc" % ( get.installDIR(), get.srcVERSION()), "_emul32", "usr")
            pisitools.dosed("%s/usr/bin/icu-config-32" % get.installDIR(), "_emul32", "usr")
        return

    pisitools.dohtml("../*.html")
