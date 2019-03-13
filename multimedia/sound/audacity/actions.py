#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "audacity-minsrc-%s" % get.srcVERSION()

def setup():
    shelltools.cd("lib-src/portmixer")
    autotools.autoreconf("-vfi")
    shelltools.cd("../..")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    shelltools.export("LIBS", "-lavcodec")
    #shelltools.export("WX_CONFIG=wx-config-gtk3 ./configure", "/usr/bin/wxconfig")
    autotools.configure("--enable-unicode \
                         WX_CONFIG=wx-config-gtk3 \
                         --enable-nyquist \
                         --enable-ladspa \
                         --with-lib-preference='system local' \
                         --with-libsndfile=system \
                         --prefix=/usr \
                         --docdir=/usr/share/doc/audacity \
                         --with-expat=system \
                         --with-libsamplerate \
                         --with-lame=system \
                         --with-libvorbis \
                         --with-libmad \
                         --with-libflac \
                         --with-libid3tag \
                         --with-sbsms \
                         --with-soundtouch \
                         --with-libvamp \
                         --with-libtwolame \
                         --with-ffmpeg=system \
                         --with-midi \
                         --with-taglib \
                         --without-lv2 \
                         --with-portmixer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/audacity/help/manual")
