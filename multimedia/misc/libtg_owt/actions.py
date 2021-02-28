#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("tg_owt-*", "tg-owt-%s" % get.srcVERSION())
    #shelltools.system("git clone https://chromium.googlesource.com/webm/libvpx")
    #shelltools.system("git clone https://chromium.googlesource.com/libyuv/libyuv")
    shelltools.cd("tg-owt-%s" % get.srcVERSION())
    
    shelltools.move("../libvpx/*", "src/third_party/libvpx/source/libvpx")
    shelltools.move("../libyuv/*", "src/third_party/libyuv")
    
    pisitools.flags.add("-fPIC")
    cmaketools.configure("-G Ninja -DCMAKE_BUILD_TYPE=Release \
                                    -DCMAKE_INSTALL_PREFIX=/usr \
                                    -DTG_OWT_SPECIAL_TARGET=linux \
                                    -DTG_OWT_LIBJPEG_INCLUDE_PATH=/usr/include \
                                    -DTG_OWT_OPENSSL_INCLUDE_PATH=/usr/include \
                                    -DTG_OWT_OPUS_INCLUDE_PATH=/usr/include/opus \
                                    -DTG_OWT_FFMPEG_INCLUDE_PATH=/usr/include")

def build():
    #shelltools.cd("%s" % get.workDIR())
    #shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    shelltools.system("ninja")

def install():
    #shelltools.cd("%s" % get.workDIR())
    #shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    pisitools.dodoc("LICENSE")
