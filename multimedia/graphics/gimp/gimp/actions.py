#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("app/text/gimpfont.c", "freetype/tttables.h", "freetype2/tttables.h")
    #autotools.autoreconf("-fi")
    autotools.configure("--disable-gtk-doc \
                         --disable-altivec \
                         --disable-alsatest \
                         --enable-python \
                         --enable-default-binary \
                         --enable-mmx \
                         --enable-sse \
                         --enable-mp \
                         --with-linux-input \
                         --with-libmng \
                         --with-webkit \
                         --with-openexr \
                         --with-alsa \
                         --with-aa \
                         --with-x")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Add illustrator and other mime types
    pisitools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README", "INSTALL", "LICENSE")
