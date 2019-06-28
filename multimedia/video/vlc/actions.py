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
    # Make it build with libtool 1.5
    #shelltools.system("rm -rf m4/lt* m4/libtool.m4")
    shelltools.system("sed -i '/DEPRECATED/s:^://:'  modules/text_renderer/freetype/text_layout.c")
    #shelltools.system("export CFLAGS+=-I/usr/include/samba-4.0")
    #shelltools.system("export CPPFLAGS+=-I/usr/include/samba-4.0")
    #shelltools.system("export CXXFLAGS+=-std=c++11")

    shelltools.export("AUTOPOINT", "true")
    #shelltools.export("CC", "clang")
    #shelltools.export("CXX", "clang++")
    shelltools.export("LDFLAGS", "-L/usr/lib -llua")
    shelltools.export("CFLAGS", "-I/usr/include/samba-4.0")
    shelltools.export("CPPFLAGS", "-I/usr/include/samba-4.0")
    shelltools.export("CXXFLAGS", "-I/usr/include/samba-4.0 -std=c++11")
    shelltools.export("LUAC", "/usr/bin/luac")
    shelltools.export("LUA_LIBS", "$(pkg-config --libs lua)")
    shelltools.export("RCC", "/usr/bin/rcc-qt5")
    shelltools.system("./bootstrap")
    #autotools.autoreconf("-vfi")
    autotools.rawConfigure("\
                            --prefix=/usr \
                            --libdir=/usr/lib \
                            --sysconfdir=/etc \
                            --with-kde-solid=/usr/share/solid/actions/ \
                            --with-default-font-family=Sans \
                            --with-default-monospace-font-family=Monospace \
                            --with-default-font=/usr/share/fonts/dejavu/DejaVuSans.ttf \
                            --with-default-monospace-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                            --with-x \
                              BUILDCC=gcc \
                              LUAC=luac  LUA_LIBS='`pkg-config --libs lua`' \
                              RCC=/usr/bin/rcc \
                            --disable-asdcp \
                            --disable-coverage \
                            --disable-cprof \
                            --disable-crystalhd \
                            --disable-decklink \
                            --disable-goom \
                            --disable-kai \
                            --disable-kva \
                            --disable-maintainer-mode \
                            --disable-opensles \
                            --disable-rpi-omxil \
                            --disable-shine \
                            --disable-sndio \
                            --disable-vsxu \
                            --disable-wasapi \
                            --disable-altivec \
                            --disable-dependency-tracking \
                            --disable-optimizations \
                            --disable-jack \
                            --disable-oss \
                            --disable-opencv \
                            --disable-rpath \
                            --disable-static \
                            --disable-update-check \
                            --disable-silent-rules \
                            --disable-mfx \
                            --enable-ncurses \
                            --enable-a52 \
                            --enable-aa \
                            --enable-alsa \
                            --enable-archive \
                            --enable-avcodec \
                            --enable-avformat \
                            --enable-postproc \
                            --enable-bluray \
                            --enable-dc1394 \
                            --enable-dbus \
                            --enable-dca \
                            --enable-dvbpsi \
                            --enable-dvdnav \
                            --enable-dvdread \
                            --enable-faad \
                            --enable-fast-install \
                            --enable-flac \
                            --enable-freetype \
                            --enable-fribidi \
                            --enable-gnutls \
                            --enable-libcddb \
                            --enable-libmpeg2 \
                            --enable-libxml2 \
                            --enable-lirc \
                            --enable-libva \
                            --enable-live555 \
                            --enable-lua \
                            --enable-mad \
                            --enable-mod \
                            --enable-mpc \
                            --enable-nls \
                            --enable-ogg \
                            --enable-opus \
                            --enable-png \
                            --enable-projectm \
                            --enable-pulse \
                            --enable-realrtsp \
                            --enable-screen \
                            --enable-sftp \
                            --enable-schroedinger \
                            --enable-shared \
                            --enable-smbclient \
                            --enable-sout \
                            --enable-speex \
                            --enable-svg \
                            --enable-theora \
                            --enable-twolame \
                            --enable-upnp \
                            --enable-v4l2 \
                            --enable-vlc \
                            --enable-vcd \
                            --enable-mtp \
                            --enable-vlm \
                            --enable-vorbis \
                            --enable-x264 \
                            --enable-x265 \
                            --enable-aribsub \
                            --enable-xvideo \
                           ")
    #enable-skins2 \ --disable-qt4 \
    #shelltools.export("CFLAGS", "%s -fPIC -O2 -Wall -Wextra -DLUA_COMPAT_5_1" % get.CFLAGS())
    
    # for fix unused dependency
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "COPYING")
