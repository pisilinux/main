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
    # Remove local copies for system libs
    for directory in ["cups/libs", "jpeg", "lcms2mt", "libpng", "openjpeg", "tiff", "zlib"]:
        shelltools.unlinkDir(directory)

    #pisitools.flags.add("-fno-strict-aliasing")

    autotools.autoreconf("-fi")

    options = "--with-x \
               --with-ijs \
               --disable-gtk \
               --with-libpaper \
               --with-jbig2dec \
               --enable-freetype \
               --with-drivers=ALL \
               --enable-fontconfig \
               --with-system-libtiff \
               --disable-compile-inits \
                --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/cups/fonts:/usr/share/fonts/TTF:/usr/share/fonts/Type1:/usr/share/poppler/cMap/*"
    
    options += " --disable-cups --includedir=/usr/include --libdir=/usr/lib32" if get.buildTYPE() == "emul32" else " --enable-cups"

    autotools.configure(options)

    shelltools.cd("ijs/")
    pisitools.dosed("configure.ac", "AM_PROG_CC_STDC", "AC_PROG_CC")
    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --enable-shared \
                       --disable-static \
                       --mandir=/usr/share/man")

def build():
    autotools.make("-C ijs")
    autotools.make("so")
    autotools.make("-j1")
    if not get.buildTYPE() == "emul32": autotools.make("cups")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")
    if not get.buildTYPE() == "emul32": autotools.rawInstall("-C ijs DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("LICENSE", "doc/COPYING")
