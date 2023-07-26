#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system('sed -i "/doxygen.sh/d" "spice-0.15.0/meson.build"')
    mesontools.configure()

def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()

    #shelltools.copytree("%s/usr/share/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    #pisitools.removeDir("/usr/share/pkgconfig")
    pisitools.dodoc("LICENSE", "README.rst")
