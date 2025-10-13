#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    shelltools.system("sed -e 's/libsystemd/libelogind/' \
                           -i plugins/power/test.py")
    # shelltools.system("sed -e 's/(backlight->logind_proxy)/(0)/' \
                           # -i plugins/power/gsd-backlight.c")

    mesontools.configure("-Dsystemd=false")

def build():
    mesontools.build

def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "MAINTAINERS")
