#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
	shelltools.system("./configure --prefix=/usr \
                            --mandir=/usr/share/man \
                            --disable-debug \
                            --disable-static \
                            --disable-stripping \
                            --enable-version3 \
                            --enable-nonfree \
                            --enable-avfilter \
                            --enable-avresample \
                            --enable-frei0r \
                            --enable-gnutls \
                            --enable-gpl \
                            --enable-libaom \
                            --enable-libass \
                            --enable-libbluray \
                            --enable-libbs2b \
                            --enable-libcelt \
                            --enable-libcdio \
                            --enable-libcodec2 \
                            --enable-libdav1d \
                            --enable-libdavs2 \
                            --enable-libdc1394 \
                            --enable-libfdk-aac \
                            --enable-libflite \
                            --enable-libfontconfig \
                            --enable-libfreetype \
                            --enable-libgme \
                            --enable-libgsm \
                            --enable-libiec61883 \
                            --enable-libilbc \
                            --enable-libkvazaar \
                            --enable-liblensfun \
                            --enable-libmodplug \
                            --enable-libmp3lame \
                            --enable-libopencore_amrnb \
                            --enable-libopencore_amrwb \
                            --enable-libopenjpeg \
                            --enable-libopenmpt \
                            --enable-libopus \
                            --enable-libpulse \
                            --enable-librsvg \
                            --enable-librubberband \
                            --enable-librtmp \
                            --enable-libshine \
                            --enable-libsnappy \
                            --enable-libsoxr \
                            --enable-libspeex \
                            --enable-libtheora \
                            --enable-libvidstab \
                            --enable-libv4l2 \
                            --enable-libvo-amrwbenc \
                            --enable-libvorbis \
                            --enable-libvpx \
                            --enable-libx264 \
                            --enable-libx265 \
                            --enable-libxavs \
                            --enable-libxavs2 \
                            --enable-libxcb \
                            --enable-libxvid \
                            --enable-libzimg \
                            --enable-pic \
                            --enable-postproc \
                            --enable-runtime-cpudetect \
                            --enable-shared \
                            --enable-swresample \
                            --enable-vdpau \
                            --enable-openal \
                            --enable-libdrm \
                            --enable-libmfx \
                            --enable-nvdec \
                            --enable-nvenc \
                            --enable-vaapi \
                            --enable-vdpau \
                            --enable-omx \
                            --extra-ldflags='-lasound -lm' ")

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')
    autotools.make("doc/ff{mpeg,play}.1")

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")
    
    pisitools.dodoc("Changelog", "README.md", "LICENSE.md", "COPYING*")
