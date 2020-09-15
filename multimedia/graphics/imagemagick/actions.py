#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

KeepSpecial=["libtool"]

def setup():
    pisitools.dosed("configure.ac", "AC_PATH_XTRA")
    autotools.autoreconf("-fi")

    pisitools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure("--with-x \
                         --with-fpx \
                         --with-jp2 \
                         --with-xml \
                         --with-wmf \
                         --with-djvu \
                         --with-perl \
                         --with-zlib \
                         --with-rsvg \
                         --with-tiff \
                         --with-jpeg \
                         --with-gslib \
                         --with-lcms2 \
                         --with-bzlib \
                         --without-dps \
                         --enable-hdri \
                         --without-fpx \
                         --with-modules \
                         --with-threads \
                         --without-jbig \
                         --enable-shared \
                         --disable-static \
                         --with-magick_plus_plus \
                         --docdir=/usr/share/doc/imagemagick \
                         --with-perl-options='INSTALLDIRS=vendor' \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript")

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")

    pisitools.remove("/usr/lib/*.la")

    perlmodules.removePacklist()
    perlmodules.removePodfiles()