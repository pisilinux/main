# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "mozjs%s/js/src" % get.srcVERSION()

shelltools.export("SHELL","/bin/sh")
WorkDir = "firefox-%s" %get.srcVERSION()

def setup():
   shelltools.export("CC", "gcc")
   shelltools.export("CXX", "g++")

   shelltools.system("mkdir -p build-js")
   shelltools.cd("build-js")

   shelltools.system("../js/src/configure \
                      --prefix=/usr \
                      --libdir=/usr/lib \
                      --enable-readline \
                      --with-intl-api \
                      --disable-debug \
                      --disable-debug-symbols \
                      --disable-jemalloc \
                      --disable-strip  \
                      --enable-hardening \
                      --enable-linker=gold \
                      --enable-optimize \
                      --enable-readline \
                      --enable-release \
                      --enable-shared-js \
                      --enable-tests \
                      --with-intl-api \
                      --with-system-zlib \
                      --with-system-nspr \
                      --without-system-icu")

def build():
    shelltools.cd("build-js")
    autotools.make()

def check():
    shelltools.cd("build-js")


def install():
    shelltools.cd("build-js")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/*.ajs")

    shelltools.cd("..")
    pisitools.dodoc("README*")
