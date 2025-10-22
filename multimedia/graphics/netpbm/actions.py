#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

def setup():
    shelltools.copy("config.mk.in", "config.mk")

    shelltools.system("sed -i 's|misc|share/netpbm|' common.mk")
    shelltools.system("sed -e 's|/sharedlink|/lib|' -i lib/Makefile")

    shelltools.echo("config.mk", "STATICLIB_TOO=N")
    shelltools.echo("config.mk", "CFLAGS_SHLIB += -fPIC")
    shelltools.echo("config.mk", "TIFFLIB = libtiff.so")
    shelltools.echo("config.mk", "JPEGLIB = libjpeg.so")
    shelltools.echo("config.mk", "PNGLIB = libpng.so")
    shelltools.echo("config.mk", "ZLIB = libz.so")
    shelltools.echo("config.mk", "JBIGLIB = /usr/lib/libjbig.a")
    pisitools.cflags.add("-std=c17")

def build():
    autotools.make("CFLAGS+='%s'" % get.CFLAGS())

def install():
    a = "install-run install-dev"
    autotools.rawInstall("pkgdir=%s/usr %s" % (get.installDIR(), a))

    pisitools.dodoc("doc/copyright_summary", "doc/GPL_LICENSE.txt")
