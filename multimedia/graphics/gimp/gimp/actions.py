#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("app/text/gimpfont.c", "freetype/tttables.h", "freetype2/tttables.h")
    #autotools.autoreconf("-fi")
    mesontools.configure("-Denable-default-bin=enabled \
                         -Dlinux-input=enabled \
                         -Dmng=enabled \
                         -Dopenexr=enabled \
                         -Dalsa=enabled \
                         -Daa=enabled \
                         -Dheadless-tests=disabled \
                         ")
    # --with-webkit \

    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Add illustrator and other mime types
    # pisitools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    # "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README", "INSTALL", "LICENSE")
