#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

i = ''.join([
    ' USE_SYSTEM_LIBS=yes',
    ' USE_SYSTEM_GLUT=no',
    ' USE_SYSTEM_LCMS2=no',
    ' USE_SYSTEM_GUMBO=no',
    ' USE_SYSTEM_JBIG2DEC=no',
    ' shared=yes '
    ])

def build():
    shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
    shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
    # remove bundled packages, use our system libraries
    shelltools.system("rm -rf thirdparty/{curl,freetype,harfbuzz,libjpeg,openjpeg,zlib}")

    autotools.make("prefix=/usr %s" % i)

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr %s" % (get.installDIR(), i))

    pisitools.dodoc("CHANGES", "COPYING", "README")
