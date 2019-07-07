#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    options = "-DCMAKE_BUILD_TYPE=Release \
               -DCMAKE_INSTALL_PREFIX=/usr \
               -DCMAKE_INSTALL_LIBDIR=lib \
               -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
               -DENABLE_XPDF_HEADERS=ON \
              "

    if get.buildTYPE() == "emul32":
        options = " -DCMAKE_INSTALL_LIBDIR=/usr/lib32 \
                    -DCMAKE_INSTALL_PREFIX=/emul32 \
                    -DENABLE_QT5=OFF \
                    -DENABLE_LIBCURL=OFF"

    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        #pisitools.insinto("/usr/lib32", "poppler/.libs/libpoppler.so*")
        #pisitools.insinto("/usr/lib32", "glib/.libs/libpoppler-glib.so*")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), get.emul32prefixDIR(), get.defaultprefixDIR())
        return
    
        pisitools.removeDir("/usr/share/gtk-doc")
        pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
