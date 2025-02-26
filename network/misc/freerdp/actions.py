#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir="FreeRDP-%s" % get.srcVERSION()

def setup():
    # shelltools.system("mkdir build")
    # shelltools.system("cd build")
    cmaketools.configure("-B build -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DWITH_LIBSYSTEMD=OFF \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DWITH_DSP_FFMPEG=ON \
                          -DWITH_FFMPEG=ON \
                          -DWITH_PULSE=ON \
                          -DWITH_CUPS=ON \
                          -DWITH_PCSC=ON \
                          -DWITH_JPEG=ON \
                          -DWITH_SERVER=ON \
                          -DWITH_SWSCALE=ON \
                          -DWITH_CHANNELS=ON \
                          -D UWAC_FORCE_STATIC_BUILD=ON  \
                          -D RDTK_FORCE_STATIC_BUILD=ON \
                          -DWITH_BINARY_VERSIONING=ON \
                          -DWITH_CLIENT_CHANNELS=ON \
                          -DWITH_SERVER_CHANNELS=ON \
                          -DCHANNEL_URBDRC_CLIENT=ON")

def build():
    shelltools.cd("build")
    cmaketools.make()

def check():
    pass

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    # cmaketools.install()
    
    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README*", )
