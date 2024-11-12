#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
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
                          -DWITH_CLIENT_CHANNELS=ON \
                          -DWITH_SERVER_CHANNELS=ON \
                          -DCHANNEL_URBDRC_CLIENT=ON")

def build():
    cmaketools.make()

def check():
    pass

def install():
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    cmaketools.install()
    
    pisitools.dodoc("LICENSE", "README*", )
