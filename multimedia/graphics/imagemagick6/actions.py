#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

KeepSpecial=["libtool"]

j = "--with-lqr \
    --with-wmf \
    --with-xml \
    --with-perl \
    --with-rsvg \
    --with-webp \
    --without-gvc \
    --prefix=/usr \
    --enable-hdri \
    --without-dps \
    --without-fpx \
    --with-modules \
    --with-openexr \
    --with-openjp2 \
    --without-djvu \
    --without-fftw \
    --enable-opencl \
    --without-gslib \
    --sysconfdir=/etc \
    --without-autotrace \
    PSDelegate=/usr/bin/gs \
    XPSDelegate=/usr/bin/gxps \
    PCLDelegate=/usr/bin/gpcl6 \
    --with-perl-options=INSTALLDIRS=vendor \
    --with-dejavu-font-dir=/usr/share/fonts/dejavu \
    --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
    PKG_CONFIG='/usr/bin/env PKG_CONFIG_PATH=/usr/lib/imagemagick6/pkgconfig pkg-config' \
    "

def setup():
    pisitools.dosed("configure.ac", "AC_PATH_XTRA")
    autotools.autoreconf("-fi")

    pisitools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure(j)
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s pkgconfigdir=/usr/lib/%s/pkgconfig" % (get.installDIR(), get.srcNAME()))

    pisitools.dodoc("LICENSE", "README*")

    pisitools.remove("/usr/lib/*.la")

    # to prevent conflict, remove binaries, we can get them from latest ImageMagick
    pisitools.removeDir("/usr/bin")
    # to prevent conflict, remove man files, we can get them from latest ImageMagick
    pisitools.removeDir("/usr/share/man")
    # to prevent conflict, remove conflicting perl files
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
    pisitools.removeDir("/usr/lib/perl5")
