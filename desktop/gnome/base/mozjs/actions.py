# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "mozjs%s/js/src" % get.srcVERSION()

shelltools.export("SHELL","/bin/sh")
WorkDir = "firefox-%s" %get.srcVERSION()

def setup():
   shelltools.system("sed -i 's|/usr/local|/usr|g' nsprpub/configure")
   #shelltools.cd("js/src")
   #shelltools.system("sed -i 's/(defined\((@TEMPLATE_FILE)\))/\1/' config/milestone.pl ")
   shelltools.export("CC", "gcc")
   shelltools.export("CXX", "g++")

   shelltools.system("mkdir -p build-js")
   shelltools.cd("build-js")
   shelltools.export("ac_default_prefix", "/usr")
   shelltools.system("sh ../js/src/configure \
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
                     # --prefix=/usr \

def build():
    shelltools.cd("build-js")
    autotools.make("prefix=/usr")

# def check():
    # shelltools.cd("build-js")

    #autotools.make("-C js/src check-jstests")
    #autotools.make("-C js/src check-jit-test")


def install():
    shelltools.cd("build-js")
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    pisitools.remove("/usr/lib/*.ajs")

    pisitools.dosym("/usr/lib/libmozjs-143.so", "/usr/lib/libmozjs-143.so.0")

    pisitools.dosed("%s/usr/bin/js128-config" % get.installDIR(), "usr/local", "usr")
    pisitools.dosed("%s/usr/lib/pkgconfig/mozjs-143.pc" % get.installDIR(), "usr/local", "usr")

    #for polkit
    #pisitools.rename("/usr/lib/pkgconfig/mozjs-..pc", "mozjs-17.0.pc")
    #pisitools.remove("usr/lib/libmozjs-..a")

    shelltools.cd("..")
    pisitools.dodoc("README*")

    # add link for polkit
    #pisitools.dosym("libmozjs-..so", "/usr/lib/libmozjs-17.0.so")
