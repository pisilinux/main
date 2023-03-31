#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' --mandir=/usr/share/man',
    ' --disable-debug',
    ' --disable-static',
    ' --disable-stripping',
    ' --disable-liblensfun',
    ' --enable-libpulse',
    ' --enable-version3',
    ' --enable-gpl',
    ' --enable-shared',
    ' --enable-frei0r',
    ' --enable-ladspa',
    ' --enable-nonfree',
    ' --enable-avfilter',
    ' --enable-pic',
    ' --enable-libaom',
    ' --enable-libjxl',
    ' --enable-libbs2b',
    ' --enable-libass',
    ' --enable-libaribb24',
    ' --enable-libcelt',
    ' --enable-libcdio',
    ' --enable-libcodec2',
    ' --enable-libbluray',
    ' --enable-libdav1d',
    ' --enable-libdavs2',
    ' --enable-libdc1394',
    ' --enable-libfdk-aac',
    ' --enable-libflite',
    ' --enable-libfribidi',
    ' --enable-libfreetype',
    ' --enable-libfontconfig',
    ' --enable-libgme',
    ' --enable-libgsm',
    ' --enable-libilbc',
    ' --enable-libjack',
    ' --enable-libkvazaar',
    ' --enable-libmodplug',
    ' --enable-libmp3lame',
    ' --enable-libiec61883',
    ' --enable-libopus',
    ' --enable-libopenjpeg',
    ' --enable-librsvg',
    ' --enable-librubberband',
    ' --enable-librtmp',
    ' --enable-libshine',
    ' --enable-libsnappy',
    ' --enable-libsoxr',
    ' --enable-libspeex',
    ' --enable-libtheora',
    ' --enable-libopencore_amrnb',
    ' --enable-libopencore_amrwb',
    ' --enable-libtwolame',
    ' --enable-libvidstab',
    ' --enable-libv4l2',
    ' --enable-libvpx',
    ' --enable-libvorbis',
    ' --enable-libwebp',
    ' --enable-libxavs',
    ' --enable-libxavs2',
    ' --enable-libxcb',
    ' --enable-libxvid',
    ' --enable-libx264',
    ' --enable-libx265',
    ' --enable-libvo-amrwbenc',
    ' --enable-libxml2',
    ' --enable-libzmq',
    ' --enable-libzimg',
    ' --enable-librav1e',
    ' --enable-postproc',
    ' --enable-runtime-cpudetect',
    ' --enable-libsvtav1',
    ' --enable-swresample',
    ' --enable-vdpau',
    ' --enable-openal',
    ' --enable-opencl',
    ' --enable-openssl',
    ' --enable-libdrm',
    ' --enable-libmfx',
    ' --enable-nvenc',
    ' --enable-nvdec',
    ' --enable-vaapi',
    ' --enable-libsrt',
    ' --enable-omx',
    ' --extra-ldflags="-lasound -lm" '
    ])

def setup():
    shelltools.system("./configure %s" % i)

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')
    autotools.make("doc/ff{mpeg,play}.1")

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")

    pisitools.dodoc("Changelog", "MAINTAINERS")
