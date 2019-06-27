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
                            --enable-avfilter \
                            --enable-avresample \
                            --enable-fontconfig \
                            --enable-gnutls \
                            --enable-gpl \
                            --enable-libass \
                            --enable-libbluray \
                            --enable-libfdk-aac \
                            --enable-libfreetype \
                            --enable-libgsm \
                            --enable-libmodplug \
                            --enable-libmp3lame \
                            --enable-libopencore_amrnb \
                            --enable-libopencore_amrwb \
                            --enable-libopenjpeg \
                            --enable-libopus \
                            --enable-libpulse \
                            --enable-librtmp \
                            --enable-libspeex \
                            --enable-libtheora \
                            --enable-libv4l2 \
                            --enable-libvorbis \
                            --enable-libvpx \
                            --enable-libx264 \
                            --enable-libx265 \
                            --enable-libxvid \
                            --enable-pic \
                            --enable-postproc \
                            --enable-runtime-cpudetect \
                            --enable-shared \
                            --enable-swresample \
                            --enable-vdpau \
                            --enable-version3 \
                            --enable-libdc1394 \
                            --enable-libcelt \
                            --enable-frei0r \
                            --enable-libcdio \
                            --enable-libvo-amrwbenc \
                            --enable-nonfree")

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')
    autotools.make("doc/ff{mpeg,play}.1")

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")
    
    pisitools.dodoc("Changelog", "README.md", "LICENSE.md", "COPYING*")
