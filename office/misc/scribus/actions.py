#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get, shelltools
    
def setup():
    shelltools.chmod("scribus/pageitem_latexframe.h")
    pisitools.dosed("CMakeLists.txt", "\"share\/doc\/\$\{MAIN_DIR_NAME\}.*", "\"share/doc/${MAIN_DIR_NAME}/\")")
    
    cmaketools.configure("-B build -DWITH_PODOFO=ON \
                          -DWANT_HUNSPELL=ON \
                          -DWANT_DISTROBUILD=YES \
                          -DWANT_GRAPHICSMAGICK=ON \
                          -DWANT_CPP17=ON \
                          -DCMAKE_CXX_STANDARD=17 \
                          -DWANT_CCACHE=YES \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DWANT_QT5SUPPORT=ON")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.insinto("/usr/share/applications", "scribus.desktop")
    pisitools.insinto("/usr/share/pixmaps", "resources/iconsets/1_5_1/scribus.png")
    pisitools.insinto("/usr/share/pixmaps", "resources/iconsets/1_5_0/scribusdoc.png", "x-scribus.png")

    pisitools.insinto("/usr/share/scribus/icons/1_5_1", "resources/iconsets/1_5_0/lab.png")
    pisitools.insinto("/usr/share/scribus/icons/1_5_1", "resources/iconsets/1_5_0/spot.png")
    pisitools.insinto("/usr/share/scribus/icons/1_5_1", "resources/iconsets/1_5_0/register.png")
    pisitools.insinto("/usr/share/scribus/icons/1_5_1", "resources/iconsets/1_5_0/DrawFreeLine.png")
