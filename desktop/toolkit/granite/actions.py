#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    # pisitools.dosym("/usr/bin/granite-7-demo", "/usr/bin/granite-demo")
    # pisitools.dosym("/usr/lib/pkgconfig/granite-7.pc", "/usr/lib/pkgconfig/granite.pc")

    pisitools.dodoc("COPYING", "README.md")
