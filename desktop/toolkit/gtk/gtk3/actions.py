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
    shelltools.unlink('testsuite/gtk/gtkresources.c')
    options = "--prefix=/usr             \
               --sysconfdir=/etc         \
               --enable-x11-backend \
               --enable-broadway-backend \
               --enable-wayland-backend \
              "

    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/bin32 \
                     --sbindir=/usr/sbin32 \
                     --enable-colord=no \
                   "

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CC())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS().replace("-fomit-frame-pointer",""))
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

        pisitools.dosed("configure.ac", "cups-config", "cups-config-32bit")

    autotools.autoreconf("-fiv")
    autotools.configure(options)

    pisitools.dosed("libtool", "( -shared )", r" -Wl,-O1,--as-needed\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove empty dir
    pisitools.removeDir("/usr/share/man")
    pisitools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

    if get.buildTYPE() == "emul32":
        for binaries in ["gtk-query-immodules-3.0"]:
            pisitools.domove("/usr/bin/%s" % binaries, "/usr/bin/", "%s-32bit" % binaries)
        pisitools.removeDir("/usr/bin32")
    pisitools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")
