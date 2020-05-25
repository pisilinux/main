#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "audacity-minsrc-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    shelltools.cd("lib-src/portmixer")
    shelltools.cd("../..")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    shelltools.export("LIBS", "-lavcodec")
    #shelltools.export("WX_CONFIG=wx-config-gtk3 ./configure", "/usr/bin/wxconfig")
    # suppress compiler warnings
    pisitools.cxxflags.add("-Wno-unused-result -Wno-implicit-int -Wno-format-overflow -Wno-return-type -Wno-format-truncation -Wno-deprecated-declarations -Wno-unknown-pragmas -Wno-maybe-uninitialized -Wno-strict-prototypes -Wno-comment -Wno-implicit-function-declaration -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -Wno-enum-compare -Wno-aligned-new -Wno-class-memaccess -Wno-unused-but-set-variable -Wno-misleading-indentation -Wno-unused-variable -Wno-reorder -Wno-unused-function -Wno-sign-compare -Wno-unused-value -Wno-pessimizing-move -Wno-reorder -Wno-switch")
    autotools.configure("--enable-unicode \
                         --with-midi \
                         --with-sbsms \
                         --prefix=/usr \
                         --with-libmad \
                         --with-taglib \
                         --without-lv2 \
                         --with-libvamp \
                         --with-libflac \
                         --enable-ladspa \
                         --enable-nyquist \
                         --with-libvorbis \
                         --with-libid3tag \
                         --with-soundtouch \
                         --with-libtwolame \
                         --with-lame=system \
                         --with-expat=system \
                         --with-libsamplerate \
                         --with-ffmpeg=system \
                         --with-libsndfile=system \
                         --docdir=/usr/share/doc/audacity \
                         WX_CONFIG=/usr/bin/wx-config-gtk3 \
                         --with-lib-preference='system local' \
                         --with-portmixer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/audacity/help/manual")