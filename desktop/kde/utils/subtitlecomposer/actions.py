#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools



def setup():
    shelltools.system("export PKG_CONFIG_PATH=/usr/lib/ffmpeg4.4/pkgconfig")
    cmaketools.configure("-B build -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DKDE_INSTALL_LIBDIR=lib \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
            -DBUILD_TESTING:BOOL=OFF \
        -DFFMPEG_AVCODEC_LIBRARY:FILEPATH=/usr/lib//usr/lib/ffmpeg4.4/libavcodec.so \
        -DFFMPEG_AVFORMAT_LIBRARY:FILEPATH=/usr/lib/ffmpeg4.4/libavformat.so \
        -DFFMPEG_AVUTIL_LIBRARY:FILEPATH=/usr/lib/ffmpeg4.4/libavutil.so \
        -DFFMPEG_SWRESAMPLE_LIBRARY:FILEPATH=/usr/lib/ffmpeg4.4/libswresample.so \
        -DFFMPEG_SWSCALE_LIBRARY:FILEPATH=/usr/lib/ffmpeg4.4/libswscale.so \
        -DQT_MAJOR_VERSION=6 -DFFMPEG_AVCODEC_INCLUDE_DIR=/usr/include/ffmpeg4.4 \
        -DFFMPEG_AVFORMAT_INCLUDE_DIR=/usr/include/ffmpeg4.4 \
        -DFFMPEG_SWRESAMPLE_INCLUDE_DIR=/usr/include/ffmpeg4.4 \
        -DFFMPEG_SWSCALE_INCLUDE_DIR=/usr/include/ffmpeg4.4 \
        -DFFMPEG_AVUTIL_INCLUDE_DIR=/usr/include/ffmpeg4.4")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.domo("po/tr.po", "tr", "subtitlecomposer.mo")

    pisitools.dodoc("LICENSES/*", "LICENSE", "README.*")
