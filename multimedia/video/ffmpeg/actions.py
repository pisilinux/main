#!//usr/bin/python
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
                            --enable-frei0r \
                            --enable-gpl \
                            --enable-ladspa \
                            --enable-libaom \
                            --enable-libaribb24 \
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
                            --enable-libfribidi \
                            --enable-libgme \
                            --enable-libgsm \
                            --enable-libiec61883 \
                            --enable-libilbc \
                            --enable-libjack \
                            --enable-libkvazaar \
                            --disable-liblensfun \
                            --enable-libmodplug \
                            --enable-libmp3lame \
                            --enable-libopencore_amrnb \
                            --enable-libopencore_amrwb \
                            --enable-libopenjpeg \
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
                            --enable-libtwolame \
                            --enable-libvidstab \
                            --enable-libv4l2 \
                            --enable-libvo-amrwbenc \
                            --enable-libvorbis \
                            --enable-libvpx \
                            --enable-libwebp \
                            --enable-libx264 \
                            --enable-libx265 \
                            --enable-libxavs \
                            --enable-libxavs2 \
                            --enable-libxcb \
                            --enable-libxvid \
                            --enable-libxml2 \
                            --enable-libzmq \
                            --enable-libzimg \
                            --enable-pic \
                            --enable-postproc \
                            --enable-librav1e \
                            --enable-runtime-cpudetect \
                            --enable-shared \
                            --enable-libsvtav1 \
                            --enable-swresample \
                            --enable-vdpau \
                            --enable-opencl \
                            --enable-openssl \
                            --enable-libdrm \
                            --enable-libmfx \
                            --enable-nvdec \
                            --enable-nvenc \
                            --enable-vaapi \
                            --enable-vdpau \
                            --enable-omx \
                            --enable-libsrt \
                            --extra-ldflags='-lasound -lm'")
                            # --enable-openal \

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')
    autotools.make("doc/ff{mpeg,play}.1")

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")

    # pisitools.dosym("/usr/lib/libavcodec.so.60", "/usr/lib/libavcodec.so.58")
    # pisitools.dosym("/usr/lib/libswscale.so.7", "/usr/lib/libswscale.so.5")
    # pisitools.dosym("/usr/lib/libavutil.so.58", "/usr/lib/libavutil.so.56")
    # pisitools.dosym("/usr/lib/libswresample.so.4", "/usr/lib/libswresample.so.3")
    # pisitools.dosym("/usr/lib/libavfilter.so.9", "/usr/lib/libavfilter.so.7")
    # pisitools.dosym("/usr/lib/libavdevice.so.60", "/usr/lib/libavdevice.so.58")
    # pisitools.dosym("/usr/lib/libavformat.so.60", "/usr/lib/libavformat.so.58")
    # pisitools.dosym("/usr/lib/libpostproc.so.57", "/usr/lib/libpostproc.so.55")
    
    pisitools.dodoc("Changelog", "README.md", "LICENSE.md", "COPYING*")
