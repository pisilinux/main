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
    shelltools.cd("tg-owt-%s" % get.srcVERSION())

    shelltools.system("git clone https://github.com/google/crc32c")
    shelltools.system("git clone https://chromium.googlesource.com/libyuv/libyuv.git")
    # shelltools.system("git clone https://github.com/cisco/libsrtp")
    shelltools.system("git clone https://github.com/abseil/abseil-cpp")

    # shelltools.system("rm -rf src/third_party/libvpx/source/libvpx")
    # shelltools.move("libvpx/*", "src/third_party/libvpx/source/libvpx")
    shelltools.move("libyuv*/*", "src/third_party/libyuv")
    shelltools.move("abseil-cpp/*", "src/third_party/abseil-cpp")
    shelltools.move("libsrtp*/*", "src/third_party/libsrtp")
    shelltools.move("crc32c/*", "src/third_party/crc32c/src")
    # shelltools.system("rm -rf src/third_party/crc32c/src")
    # shelltools.move("crc32c-1.1.2/*", "src/third_party/crc32c/src")

    pisitools.cflags.add(" -ffat-lto-objects")
    pisitools.cxxflags.add(" -ffat-lto-objects -I/usr/include/libdrm")
    cmaketools.configure("-B build -G Ninja -DCMAKE_BUILD_TYPE=Release \
                                    -DCMAKE_INSTALL_PREFIX=/usr \
                                    -DBUILD_SHARED_LIBS=OFF \
                                    -DTG_OWT_LIBJPEG_INCLUDE_PATH=/usr/include \
                                    -DTG_OWT_OPENSSL_INCLUDE_PATH=/usr/include \
                                    -DTG_OWT_OPUS_INCLUDE_PATH=/usr/include/opus \
                                    -DTG_OWT_LIBVPX_INCLUDE_PATH=/usr/include \
                                    -DTG_OWT_FFMPEG_INCLUDE_PATH=/usr/include")

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    shelltools.system("ninja")

def install():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("LICENSE")
