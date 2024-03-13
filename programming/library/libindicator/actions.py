#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.copytree("../libindicator-%s" % (get.srcVERSION().replace("_", "~")), "../libindicator-%s-gtk3" % get.srcVERSION())

    pisitools.cflags.add("-Wno-error=deprecated-declarations")
    autotools.configure("--libexecdir=/usr/lib \
                         --disable-static \
                         --disable-introspection \
                         --with-gtk=2")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

    shelltools.cd("../libindicator-%s-gtk3" % get.srcVERSION())
    pisitools.cflags.add("-Wno-error=deprecated-declarations")
    autotools.configure("--libexecdir=/usr/lib \
                         --disable-static \
                         --with-gtk=3")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")




def build():
    autotools.make()

    shelltools.cd("../libindicator-%s-gtk3" % get.srcVERSION())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../libindicator-%s-gtk3" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING", "README")
