#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
    shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
    autotools.make("prefix=/usr")

    # remove bundled packages, use our system libraries
#    shelltools.system("rm -rf thirdparty/{curl,freeglut,freetype,harfbuzz,jbig2dec,lcms2,libjpeg,mujs,openjpeg,zlib}")

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("CHANGES", "README", "COPYING")
