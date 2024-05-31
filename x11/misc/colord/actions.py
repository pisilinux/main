#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
    shelltools.system("""sed -i -e "/find_program('vapigen')/d" meson.build""")
    mesontools.configure("-Ddaemon_user=colord \
                          -Dsystemd=false \
                          -Ddocs=false \
                          -Dlibcolordcompat=true \
                          -Dman=false")

    
def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.insinto("/etc/dbus-1/system.d/","%s/usr/share/dbus-1/system.d/org.freedesktop.ColorManager.conf" % get.installDIR())
    pisitools.removeDir("/usr/share/dbus-1/system.d")

    pisitools.dodoc("AUTHORS", "MAINTAINERS", "COPYING", "RELEASE", "NEWS", "README.md")
