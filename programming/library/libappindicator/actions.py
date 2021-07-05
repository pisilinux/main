#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, shelltools, get

def setup():
    #shelltools.export("PYTHON", "/usr/bin/python3")
    shelltools.copytree("../libappindicator-%s" % (get.srcVERSION().replace("_", "~")), "../libappindicator-%s-gtk3" % get.srcVERSION())

    pisitools.dosed("src/Makefile.am", "-Werror", "")
    autotools.autoreconf("-fiv")
    autotools.configure("--with-gtk=2 \
                         --enable-introspection=no \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

    shelltools.cd("../libappindicator-%s-gtk3" % get.srcVERSION())
    pisitools.dosed("src/Makefile.am", "-Werror", "")
    autotools.autoreconf("-fiv")
    autotools.configure("--with-gtk=3 \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")


def build():
    autotools.make()

    shelltools.cd("../libappindicator-%s-gtk3" % get.srcVERSION())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../libappindicator-%s-gtk3" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog")

